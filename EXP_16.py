
from sklearn.neighbors import KNeighborsClassifier

X = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]]
y = ["A", "A", "A", "B", "B", "B"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict([[2, 3]])

print("Training completed successfully")
print("Input: [2, 3]")
print("Predicted Class:", prediction[0])
