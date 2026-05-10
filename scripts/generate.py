import os
import subprocess
import re

def run_command(cmd_args):
    result = subprocess.run(cmd_args, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.replace('\r\n', '\n')

def get_all_commands(root_help_text):
    commands =[]
    in_commands_section = False
    
    for line in root_help_text.splitlines():
        if line.startswith('Commands:'):
            in_commands_section = True
            continue
        
        if in_commands_section:
            if line.startswith('Options:') or line.startswith('Global Options:'):
                break
            
            match = re.match(r'^  ([a-z-]+)(?:\s+|$)', line)
            if match:
                commands.append(match.group(1))
                
    return commands

def process_and_save(cmd_name, output_text, out_dir):
    match = re.search(r'^(Usage:.*?(?=\nGlobal Options:|\Z))', output_text, re.MULTILINE | re.DOTALL)
    
    if match:
        extracted = match.group(1).strip()
        extracted = extracted.replace('jj.exe', 'jj')
        extracted += '\n'
        
        out_path = os.path.join(out_dir, f"{cmd_name}.md")
        
        with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(extracted)
        
        print(f"✅ Generated: {out_path}")
    else:
        print(f"⚠️ Cannot find Usage paragraph in output of {cmd_name}")

def main():
    out_dir = './skills/jj-vcs/references'
    os.makedirs(out_dir, exist_ok=True)
    
    root_help = run_command(['jj', 'help', '--no-pager'])
    
    process_and_save('help', root_help, out_dir)
    
    commands = get_all_commands(root_help)
    
    for cmd in commands:
        if cmd == 'help':
            continue
        
        cmd_output = run_command(['jj', cmd, '--help', '--no-pager'])
        process_and_save(cmd, cmd_output, out_dir)
        
    print(f"\n🎉 Done. Output: {os.path.abspath(out_dir)}")

if __name__ == '__main__':
    main()