import sys
import markdown

if __name__ == "__main__":
    
    args = sys.argv
    file = args[1]
    
    md = markdown.Markdown()
    with open(file) as f:
        before_convert = f.read()
    result = md.convert(before_convert)
    print(result)