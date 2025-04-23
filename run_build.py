import json

def create_build_list(modules: object):
    build_list=[]
    processed = set()
    
    def process_build(module_id: str):
        # if already processed ignore
        if module_id in processed:
            return
        #process module dependcies
        for d in modules[module_id]["dependencies"]:
            process_build(d)
        #only then process module
        build_list.append(module_id)
        processed.add(module_id)

    for m in modules:
        process_build(m)
    
    return build_list
        

if __name__ == "__main__":
    with open("modules.json","r") as f:
        modules = json.load(f)

    print(",".join(create_build_list(modules)))
