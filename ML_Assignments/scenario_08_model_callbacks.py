# Scenario 8: Model Callbacks
# Task: Implement an EarlyStopping callback that monitors validation loss,
# stops training after 3 epochs without improvement, and restores best weights.

from tensorflow.keras.callbacks import EarlyStopping

def get_callbacks():
    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )
    return early_stop


if __name__ == "__main__":
    print("EarlyStopping Callback Ready")