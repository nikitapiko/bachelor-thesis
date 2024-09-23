"""Custom Plotly visualizations for Streamlit"""

__version__ = "5.1"

import plotly.graph_objects as go
import streamlit as st
import time
import fear_and_greed


def gauge(gVal, gTitle="", gMode='gauge+number', gSize="FULL", gTheme="Black",
          grLow=.29, grMid=.69, gcLow='#FF1708', gcMid='#FF9400',
          gcHigh='#1B8720', xpLeft=0, xpRight=1, ypBot=0, ypTop=1,
          arBot=None, arTop=1, pTheme="streamlit", cWidth=True, sFix=None):

    if sFix == "%":
        gaugeVal = round((gVal * 100), 1)
        top_axis_range = (arTop * 100)
        bottom_axis_range = arBot
        low_gauge_range = (grLow * 100)
        mid_gauge_range = (grMid * 100)
    else:
        gaugeVal = gVal
        top_axis_range = arTop
        bottom_axis_range = arBot
        low_gauge_range = grLow
        mid_gauge_range = grMid

    if gSize == "SML":
        x1, x2, y1, y2 = .25, .25, .75, 1
    elif gSize == "MED":
        x1, x2, y1, y2 = .50, .50, .50, 1
    elif gSize == "LRG":
        x1, x2, y1, y2 = .75, .75, .25, 1
    elif gSize == "FULL":
        x1, x2, y1, y2 = 0, 1, 0, 1
    elif gSize == "CUST":
        x1, x2, y1, y2 = xpLeft, xpRight, ypBot, ypTop

    if gaugeVal <= low_gauge_range:
        gaugeColor = gcLow
    elif gaugeVal >= low_gauge_range and gaugeVal <= mid_gauge_range:
        gaugeColor = gcMid
    else:
        gaugeColor = gcHigh

    fig1 = go.Figure(go.Indicator(
        mode=gMode,
        value=gaugeVal,
        domain={'x': [x1, x2], 'y': [y1, y2]},
        number={"suffix": sFix},
        title={'text': gTitle},
        gauge={
            'axis': {'range': [bottom_axis_range, top_axis_range]},
            'bar': {'color': gaugeColor}
        }
    ))

    config = {'displayModeBar': False}
    fig1.update_traces(title_font_color=gTheme, selector=dict(type='indicator'))
    fig1.update_traces(number_font_color=gTheme, selector=dict(type='indicator'))
    fig1.update_traces(gauge_axis_tickfont_color=gTheme, selector=dict(type='indicator'))
    fig1.update_layout(margin_b=5)
    fig1.update_layout(margin_l=20)
    fig1.update_layout(margin_r=20)
    fig1.update_layout(margin_t=50)
    fig1.update_layout(margin_autoexpand=True)

    return fig1

sentiment_val_path = "/Users/nikitapiko/Documents/University/WU Wien/SBWL/Data Science/PROJECTS/SPX500/data/current_sentiment_index_value.txt"
with open(sentiment_val_path, 'r') as file:
    SENTIMENT_INDEX_VALUE = float(file.read())

logreg_val_path = "/Users/nikitapiko/Documents/University/WU Wien/SBWL/Data Science/PROJECTS/SPX500/data/logreg_current_sentiment_value.txt"
with open(logreg_val_path, 'r') as file:
    LOGREG_VALUE = float(file.read())


# Streamlit App

st.markdown(f"### Sentiment Time Span: **31.08.2023 - 02.09.2024, Last 3 Days**")

# FinBERT Sentimnet Index
hf_logo = "../img/huggingface_logo_smiley.jpg"
col1, col2 = st.columns([0.2, 0.8])

with col1:
    st.image(hf_logo, width=120)

with col2:
    st.title("S&P 500 Sentiment Index - FinBERT")



# Placeholder for the gauge
gauge_placeholder = st.empty()


# Incrementally increase the gauge value
for i in range(int(SENTIMENT_INDEX_VALUE) + 1):
    if i >= 70:
        sentiment_color = "#1B8720"
        sentiment_label = "Greed"
    elif i >= 30:
        sentiment_color = "#FF9400"
        sentiment_label = "Neutral"
    else:
        sentiment_color = "#FF1708"
        sentiment_label = "Fear"

    # Update the dynamic gauge in the same placeholder
    fig = gauge(
        gVal=i,
        gTitle=f"S&P 500 Sentiment Index - {sentiment_label}",
        gMode='gauge+number',
        gSize="FULL",
        gTheme=sentiment_color,
        grLow=30,
        grMid=70,
        gcLow='#FF1708',
        gcMid='#FF9400',
        gcHigh='#1B8720',
        arBot=0,
        arTop=100,
        pTheme="streamlit"
    )

    gauge_placeholder.plotly_chart(fig, use_container_width=True)

    # Pause for a moment to create the animation effect
    time.sleep(0.02)

# Display final sentiment label and score
st.markdown(f"### Sentiment Label: **{sentiment_label}**")
st.markdown(f"### Sentiment Score: **{SENTIMENT_INDEX_VALUE:.2f}**")


# CNN REFERENCE

cnn_tuple = fear_and_greed.get()
cnn_val = cnn_tuple[0]
cnn_descr = cnn_tuple[1]


# st.markdown(f"CNN SENTIMENT INDEX VALUE:{cnn_val}   -   {cnn_descr}")


# CNN Section
cnn_logo = "../img/cnn_logo.jpg"
cnn1, cnn2 = st.columns([0.2, 0.8])
with cnn1:
    st.image(cnn_logo, width=120)
with cnn2:
    st.title("S&P 500 Fear & Greed Index - CNN")


# Placeholder for the gauge
gauge_placeholder = st.empty()


# Incrementally increase the gauge value
for i in range(int(cnn_val) + 1):
    if i >= 70:
        sentiment_color = "#1B8720"
        sentiment_label = "Greed"
    elif i >= 30:
        sentiment_color = "#FF9400"
        sentiment_label = "Neutral"
    else:
        sentiment_color = "#FF1708"
        sentiment_label = "Fear"

    # Update the dynamic gauge in the same placeholder
    fig = gauge(
        gVal=i,
        gTitle=f"S&P 500 Sentiment Index - {sentiment_label}",
        gMode='gauge+number',
        gSize="FULL",
        gTheme=sentiment_color,
        grLow=30,
        grMid=70,
        gcLow='#FF1708',
        gcMid='#FF9400',
        gcHigh='#1B8720',
        arBot=0,
        arTop=100,
        pTheme="streamlit"
    )

    gauge_placeholder.plotly_chart(fig, use_container_width=True)

    # Pause for a moment to create the animation effect
    time.sleep(0.02)


# Display final sentiment label and score
st.markdown(f"### Sentiment Label: **{sentiment_label}**")
st.markdown(f"### Sentiment Score: **{cnn_val:.2f}**")


# ______________
# Logreg Section
logreg_logo = "../img/logreg_logo.jpg"

logreg1, logreg2 = st.columns([0.2, 0.8])

with logreg1:
    st.image(logreg_logo, width=120)

with logreg2:
    st.title("S&P 500 Fear & Greed Index - Logistic Regression")


# Placeholder for the gauge
gauge_placeholder = st.empty()


# Incrementally increase the gauge value
for i in range(int(LOGREG_VALUE) + 1):
    if i >= 70:
        sentiment_color = "#1B8720"
        sentiment_label = "Greed"
    elif i >= 30:
        sentiment_color = "#FF9400"
        sentiment_label = "Neutral"
    else:
        sentiment_color = "#FF1708"
        sentiment_label = "Fear"

    # Update the dynamic gauge in the same placeholder
    fig = gauge(
        gVal=i,
        gTitle=f"S&P 500 Sentiment Index - {sentiment_label}",
        gMode='gauge+number',
        gSize="FULL",
        gTheme=sentiment_color,
        grLow=30,
        grMid=70,
        gcLow='#FF1708',
        gcMid='#FF9400',
        gcHigh='#1B8720',
        arBot=0,
        arTop=100,
        pTheme="streamlit"
    )

    gauge_placeholder.plotly_chart(fig, use_container_width=True)

    # Pause for a moment to create the animation effect
    time.sleep(0.02)


# Display final sentiment label and score
st.markdown(f"### Sentiment Label: **{sentiment_label}**")
st.markdown(f"### Sentiment Score: **{LOGREG_VALUE:.2f}**")







# BONUS: CHAT GPT SENTIMENT INDICATOR