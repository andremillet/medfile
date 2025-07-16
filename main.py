import re
import json

def parse_med_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {}
    # Regex to find all sections, including the text until the first section
    sections = re.split(r'\n(?=\[[A-Z\s]+\])', content)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        header_match = re.match(r'\[([A-Z\s]+)\]', section)
        if header_match:
            header = header_match.group(1)
            section_content = section[len(header)+2:].strip()
            data[header] = parse_section_content(header, section_content)
        else:
            # Content before the first section (if any)
            if ' unstructured' not in data:
                data[' unstructured'] = ''
            data[' unstructured'] += section + '\n'


    return data

def parse_section_content(header, content):
    if header == "ANAMNESE":
        return parse_anamnese(content)
    # Placeholder for other sections
    return content.split('\n')

def parse_anamnese(content):
    anamnese_data = {'queixa_principal': ''}
    lines = content.split('\n')
    
    queixa_principal_lines = []
    for line in lines:
        if line.startswith('!'):
            tag_match = re.match(r'!([A-Z]+) (.*)', line)
            if tag_match:
                tag, value = tag_match.groups()
                anamnese_data[tag.lower()] = [v.strip() for v in value.split(';') if v.strip()]
        else:
            queixa_principal_lines.append(line)
    
    anamnese_data['queixa_principal'] = '\n'.join(queixa_principal_lines).strip()
    return anamnese_data

if __name__ == "__main__":
    parsed_data = parse_med_file('example.med')
    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))