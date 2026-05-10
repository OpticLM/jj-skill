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

def format_to_markdown(extracted_text):
    lines = extracted_text.splitlines()
    out =[]
    
    current_section = None
    first_item_in_section = True
    has_blank_line = False
    last_was_desc = False
    
    for line in lines:
        if not line.strip():
            has_blank_line = True
            continue
            
        if line.startswith('Usage: '):
            out.extend(['## Usage', '', line[len('Usage: '):].strip()])
            current_section = 'Usage'
            has_blank_line = False
            last_was_desc = False
            continue
            
        match_header = re.match(r'^([A-Z][A-Za-z\s]+):$', line)
        if match_header:
            current_section = match_header.group(1)
            out.extend(['', f'## {current_section}', ''])
            first_item_in_section = True
            has_blank_line = False
            last_was_desc = False
            continue
            
        if current_section and current_section != 'Usage':
            leading_spaces = len(line) - len(line.lstrip())
            
            if 0 < leading_spaces <= 7:
                if not first_item_in_section:
                    out.append('')
                
                parts = re.split(r'\s{2,}', line.strip(), maxsplit=1)
                
                out.append(f'* {parts[0]}')
                if len(parts) == 2:
                    out.append(f'  {parts[1]}')
                    last_was_desc = True
                else:
                    last_was_desc = False
                
                first_item_in_section = False
                has_blank_line = False
            
            elif leading_spaces > 7:
                stripped = line.strip()
                if last_was_desc and not has_blank_line:
                    out[-1] += f' {stripped}'
                else:
                    out.append(f'  {stripped}')
                    last_was_desc = True
                has_blank_line = False
                
            else:
                if not first_item_in_section and has_blank_line:
                    out.append('')
                out.append(line.strip())
                last_was_desc = False
                has_blank_line = False
        else:
            if has_blank_line and out and out[-1] != '':
                out.append('')
            out.append(line.strip())
            last_was_desc = False
            has_blank_line = False
            
    while out and out[0] == '':
        out.pop(0)
        
    return '\n'.join(out) + '\n'

def process_and_save(cmd_name, output_text, out_dir):
    match = re.search(r'^(Usage:.*?(?=\nGlobal Options:|\Z))', output_text, re.MULTILINE | re.DOTALL)
    
    if match:
        extracted = match.group(1).strip()
        extracted = extracted.replace('jj.exe', 'jj')
        
        markdown_content = format_to_markdown(extracted)
        
        out_path = os.path.join(out_dir, f"{cmd_name}.md")
        
        with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(markdown_content)
        
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