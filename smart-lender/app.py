from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import json
import webbrowser

app = Flask(__name__)

prediction_history=[]

# Load model
try:

    model=joblib.load(
        'models/loan_model.pkl'
    )

    with open(
        'models/feature_names.json',
        'r'
    ) as f:

        feature_names=json.load(f)

    print(
        "[✓] Model loaded successfully!"
    )

    print(
        "[✓] Features:",
        feature_names
    )

except Exception as e:

    print(
        f"[✗] Error loading model:{e}"
    )

    model=None
    feature_names=None


@app.route('/')
def home():

    return render_template(
        'index.html'
    )


@app.route(
'/predict',
methods=['POST']
)

def predict():

    try:

        data=request.json

        print(
            "\nReceived Input:"
        )

        print(data)


        features=[

            float(
                data[
                'no_of_dependents'
                ]
            ),

            float(
                data[
                'education'
                ]
            ),

            float(
                data[
                'self_employment'
                ]
            ),

            float(
                data[
                'income_annual'
                ]
            ),

            float(
                data[
                'loan_amount'
                ]
            ),

            float(
                data[
                'loan_term'
                ]
            ),

            float(
                data[
                'cibil_score'
                ]
            ),

            float(
                data[
                'residential_assets'
                ]
            ),

            float(
                data[
                'commercial_assets'
                ]
            ),

            float(
                data[
                'luxury_assets'
                ]
            ),

            float(
                data[
                'bank_assets'
                ]
            )

        ]


        features_array=np.array(
            [features]
        )


        prediction=model.predict(
            features_array
        )[0]


        probabilities=(
            model.predict_proba(
                features_array
            )[0]
        )


        confidence=(
            max(
                probabilities
            )*100
        )


        result=(
            "Approved"
            if prediction==1
            else
            "Rejected"
        )


        # Smart explanation

        reasons=[]

        cibil=float(
            data[
            'cibil_score'
            ]
        )

        income=float(
            data[
            'income_annual'
            ]
        )

        loan=float(
            data[
            'loan_amount'
            ]
        )

        bank=float(
            data[
            'bank_assets'
            ]
        )


        if cibil>=750:

            reasons.append(
            "✓ High CIBIL score"
            )

        elif cibil<600:

            reasons.append(
            "⚠ Low CIBIL score"
            )


        if income>(loan/2):

            reasons.append(
            "✓ Income supports requested loan"
            )

        else:

            reasons.append(
            "⚠ Loan amount high compared to income"
            )


        if bank>500000:

            reasons.append(
            "✓ Strong bank assets"
            )


        if result=="Rejected":

            reasons.append(
            "⚠ Higher financial risk"
            )


        # Store history

        prediction_history.append({

            "result":
            result,

            "confidence":
            round(
                confidence,
                2
            )

        })


        return jsonify({

            "prediction":
            result,

            "confidence":
            round(
                confidence,
                2
            ),

            "probability_rejected":
            round(
                probabilities[0]*100,
                2
            ),

            "probability_approved":
            round(
                probabilities[1]*100,
                2
            ),

            "reasons":
            reasons

        })


    except Exception as e:

        print(
            f"\nPrediction Error:{e}"
        )

        return jsonify({

            "error":
            str(e)

        }),500


@app.route('/history')

def history():

    return jsonify(
        prediction_history
    )


@app.route('/model_info')

def model_info():

    return jsonify({

        "model":
        "Random Forest",

        "accuracy":
        "98.13%",

        "features":
        len(
            feature_names
        )

    })


@app.route('/test')

def test():

    return jsonify({

        "status":
        "API Running",

        "model_loaded":
        model is not None

    })


if __name__=='__main__':

    print("\n"+"="*50)

    print(
        "SMART LENDER STARTING"
    )

    print("="*50)

    webbrowser.open(
        "http://127.0.0.1:5000"
    )

    app.run(

        debug=True,
        port=5000

    )