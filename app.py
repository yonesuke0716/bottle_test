from bottle import route, run

import plotly.express as px


def make_histogram(df, feature, color):
    fig = px.histogram(df, color)
    fig.update_layout(
        title=f"{feature}のヒストグラム", xaxis_title=feature, yaxis_title="Frequency"
    )
    return fig


# /plot にアクセスした場合にグラフを表示する
@route("/")
@route("/plot")
def plot():
    # データの生成
    df = px.data.iris()
    fig = make_histogram(df, feature="sepal_length", color="species")

    # グラフをHTMLとしてレンダリングする
    plot_html = fig.to_html(full_html=False)

    # レスポンスを設定する
    return plot_html


# サーバーの起動
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
