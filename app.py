from apps.template import create_app
from apps.ctr import filtering_handle
from flask import Response
import json

app = create_app()


def CreateJson(statue, message, data=None):
    if data is None:
        data = list()
    res = dict()
    res["statue"] = statue
    res["message"] = message
    res["data"] = data
    return Response(json.dumps(res), mimetype='application/json')


@app.route('/api/v1/recommend/')
@app.route('/api/v1/recommend/<uid>')
def recommend_with_id(uid=None):
    if uid is None:
        res = filtering_handle.zero_vector(6)
        return CreateJson(200, "OK", res)
    elif app.config["CTR_BACKEND"] == "Collaborative Filtering":
        res = filtering_handle.predict(uid, 6)
        return CreateJson(200, "OK", res)
    elif app.config["CTR_BACKEND"] == "PNN":
        res = filtering_handle.predict(uid, 6)
        return CreateJson(200, "OK", res)
    else:
        return CreateJson(500, "Internal Server Error")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
