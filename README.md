# build modules exercise

## run
python run_build.py

### to check not cyclic 
change https://github.com/blumus/buildModules/blob/c34946a3d0ff9cdc724638d44eeea14cb5e8a74b/modules.json#L19
```json
"D": {
        "name": "D",
        "dependencies": ["A"],
        "actions": ["printBuild"]
    },
```
to
```json
"D": {
        "name": "D",
        "dependencies": [],
        "actions": ["printBuild"]
    },
```
