from sklearn.neural_network import MLPClassifier
import joblib
import random

def get_ai_move(game_matrix, machine_symbol):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if game_matrix[i,j] == 0]
    return random.choice(empty_spots)

def get_model():
    model = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=500)
    return model

def train_model(model):
    pass
    # TODO: insert logic for training here

if __name__ == '__main__':
    model = get_model()
    joblib.dump(model, './Esercizi/tic-tac-toe-ml/tic_tac_toe_mlp.pkl')
    # print(model(np.ones((3, 3), dtype=int)).numpy())