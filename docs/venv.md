
## The folder venv (virtual environment)

Il contient 3 folders

venv/
├── bin/          # (Scripts/ sur Windows)
├── include/
├── lib/
└── pyvenv.cfg

## VENV/BIN 
C'est ici que se trouve tout ce qui active et fait tourner ton venv :

bin/
├── activate        ← le script que tu lances (source venv/bin/activate)
├── python          ← le Python isolé de ton venv
├── pip             ← le pip isolé de ton venv
└── flask           ← ajouté après pip install flask

## VENV/LIB
C'est ici que sont stockés tous tes packages installés :

lib/
└── python3.x/
    └── site-packages/
        ├── flask/        ← après pip install flask
        ├── click/

## pyvenv.cfg
Fichier de config qui définit quel Python utilise ce venv :
home = /usr/bin/python3
version = 3.11.0
