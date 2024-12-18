from flask import Flask, jsonify, request
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/pca', methods=['GET'])
def pca():
    cached_results = redis_client.get('pca_results')
    if cached_results:
        return jsonify({'cached': True, 'data': eval(cached_results)})


    #load iris dataset into a Dataframe
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)

    #perform PCA
    pca = PCA(whiten=True).fit(X)
    #Transform original data
    X_pca = pca.transform(X)

    #get all PCAs
    idx = [f'PC+{str(i+1)}' for i in range(len(pca.components_))]
    PCAs = pd.DataFrame(pca.components_, index=idx, columns=iris.feature_names)
    pcas_json = PCAs.to_json(orient='index')


    #get the variance explained by each PC
    var_explained = {'variance_explained': [f'PC{pc+1} explains {var*100:.3f}% of total variance'
                                            for pc,var in enumerate(pca.explained_variance_ratio_)]}
    redis_client.set('pca_results', str(var_explained))
    return jsonify({'cached': False, 'data': var_explained})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
