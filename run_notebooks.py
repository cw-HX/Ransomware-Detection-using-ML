import os
import glob
import nbformat
from nbclient import NotebookClient

MODEL_DIR = os.path.join(os.path.dirname(__file__), "Model")
OUT_DIR = os.path.join(MODEL_DIR, "executed")

def execute_notebook(in_path, out_path, timeout=600):
    nb = nbformat.read(in_path, as_version=4)
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3")
    cwd = os.getcwd()
    nb_dir = os.path.dirname(in_path) or cwd
    try:
        os.chdir(nb_dir)
        client.execute()
        nbformat.write(nb, out_path)
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        os.chdir(cwd)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    notebooks = glob.glob(os.path.join(MODEL_DIR, "*.ipynb"))
    notebooks = [p for p in notebooks if ".ipynb_checkpoints" not in p]
    if not notebooks:
        print("No notebooks found in Model/")
        return

    results = []
    for nb_path in notebooks:
        name = os.path.basename(nb_path)
        out_path = os.path.join(OUT_DIR, name)
        print(f"Executing {name} -> {out_path}")
        ok, err = execute_notebook(nb_path, out_path)
        if ok:
            print(f"Success: {name}")
        else:
            print(f"Failed: {name}: {err}")
        results.append((name, ok, err))

    print("\nSummary:")
    for name, ok, err in results:
        status = "OK" if ok else f"FAILED ({err})"
        print(f" - {name}: {status}")

if __name__ == '__main__':
    main()
