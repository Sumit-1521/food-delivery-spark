from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.sql import DataFrame

def get_preprocessing_stages() -> list:
    stages = []

    # Categorical columns to be indexed and encoded
    categorical_cols = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]
    
    for col in categorical_cols:
        # String Indexer
        indexer = StringIndexer(inputCol=col, outputCol=f"{col}_Index")
        stages.append(indexer)
        
        # One Hot Encoder
        encoder = OneHotEncoder(inputCols=[f"{col}_Index"], outputCols=[f"{col}_OHE"])
        stages.append(encoder)

    # Assemble features into a single vector
    feature_cols = [f"{col}_OHE" for col in categorical_cols] + ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    stages.append(assembler)

    return stages