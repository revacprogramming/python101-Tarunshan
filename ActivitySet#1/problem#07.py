text = "X-DSPAM-Confidence:    0.8475"
f=text.find("0")
print(float(text[f:f+7]))