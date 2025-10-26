import nbformat as nbf

file = "Shaunak_Eduskills AIML_1_Intro_to_Tensorflow.ipynb"

nb = nbf.read(file, as_version=4)

# Remove widget metadata safely without touching outputs
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

# Also scrub cellwise widget metadata if any
for cell in nb.get("cells", []):
    if "metadata" in cell and "widgets" in cell["metadata"]:
        del cell["metadata"]["widgets"]

nbf.write(nb, file)
print("✅ Fixed and saved:", file)