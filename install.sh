python -m venv ./env
. env/bin/activate
pip install -r packages.txt
python -m spacy download de_core_news_sm

deactivate