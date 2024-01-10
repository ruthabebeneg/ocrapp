from setuptools import setup, find_packages

setup(
    name='nom_de_votre_projet',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'opencv-python',
        'tensorflow',
        'matplotlib',
        'doctr',
    ],
    cmdclass={'install': lambda x: None},  # Ajoutez cette ligne pour éviter l'erreur
)
