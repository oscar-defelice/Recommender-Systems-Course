%%bash
if [ ! -d "../data/movielens_complete" ]; then
    wget http://files.grouplens.org/datasets/movielens/ml-latest.zip
    mkdir -p ../data/movielens_complete
    unzip -o ml-latest.zip -d ../data/movielens_complete
else
    echo "Data already downloaded"
fi
