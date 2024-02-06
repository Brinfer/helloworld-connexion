# HelloWorld Connexion

A simple project used to test the distribution of a server using pyinstaller

## Dependencies

```bash
pip install connexion connexion[flask] connexion[swagger-ui] pyinstaller
```

## Serve

To run the server execute the command:

```bash
python -m helloworld
```

## PyInstaller

The aim is to be able to distribute the server using PyInstaller, for which the following command is used:

```bash
pyinstaller\
    helloworld/__main__.py\
    --add-data helloworld/spec:spec\
    --collect-all connexion\
    --name helloworld\
    --onefile
```
