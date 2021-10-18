import pathlib
import yaml

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).resolve().parent

yaml_samples = [
    "1",
    "-1",
    "1.0",
    "-1.0",
    "0xA",
    "-0xA",
    "-0XA",
    "yes",
    "no",
    "NO",
    "-05_5:7.6",
    "-0x5_5:7.6",
    "0x5_5:7.6",
    "0x57",
    "1:2:3:4",
    "-1:2:3:4",
    "-01:2:3:4",
    "0xA01",
    "0XA01",
    "0xA_01",
    "{ 1 : 2 }",
    "{ 1 : 2}",
    "{ 1_ : 2}",
    "{ _1 : 2}",
    "{ 1 :2}",
    "{ 1: 2}",
    "{ 1:2}",
    "{1:2}",
]

def get_type(data):
    if isinstance(data, dict):
        for key, value in data.items():
            return f"{get_type(key)} -> {get_type(value)}"
    return data.__class__.__name__

def base_alpha(i):
    if i > 24:
        return base_alpha(i//24-1) + base_alpha(i%24-1)
    return chr(i + ord("a"))

def samples_iterator():
    for i, sample_text in enumerate(yaml_samples):
        index = base_alpha(i)
        yaml_document = f"\n---\n{index}: {sample_text}\n"

        data = yaml.load(yaml_document, Loader=yaml.SafeLoader)
    
        yield index, sample_text, data[index]

def markdown_inner(f, results):
    def line(cells):
        if not results:
            cells = cells[:2]
        f.write("|".join(cells))
        f.write("\n")

    line(["example", "yaml", "data", "datatype"])
    line(["--", ":--:", ":--:", ":--:"])
    for index, sample_text, data in samples_iterator():
        line([index,f"`{sample_text}`",f"`{repr(data)}`", get_type(data)])

def markdown(filename, results):
    with (DIRECTORY_OF_THIS_FILE/filename).open("w") as f:
        f.write(f"""
# Some examples of difficult to read yaml literals

While studing the source of pyyaml, I constructed some difficult to read literals.

The 'source code under test' is the method `construct_yaml_int()` in https://github.com/yaml/pyyaml/blob/master/lib/yaml/constructor.py

""")
        markdown_inner(f, results)

def interactive():
    for index, sample_text, data in samples_iterator():
        input(f"{index}: {sample_text}   ")
        print(f"  ==> {repr(data)}      {get_type(data)}")

if __name__ == "__main__":
    markdown("test_yaml.md", False)
    markdown("test_yaml_results.md", True)

    interactive()
