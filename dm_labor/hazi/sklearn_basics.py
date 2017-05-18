import numpy as np
import sklearn.metrics as sk_eval
from sklearn import linear_model as lin
from sklearn import tree
from sklearn import naive_bayes  as nb
from sklearn import neighbors
from sklearn.model_selection import train_test_split

# norm�l�s
def l2_norm(x):
    x_n = np.copy(x)
    for i in range(x[:,0].size):
        n = np.linalg.norm(x[i,:])
        if n>0:
            x_n[i,:] = x[i,:]/n
    return x_n
    
# adatok sz�tv�laszt�sa tan�t�- �s tesztadatokk�
data = np.genfromtxt('person.txt')
train_features, test_features, train_labels, test_labels = train_test_split(data[:,1:], data[:,0], test_size = 0.33, random_state=3)

# v�letlen oszt�lyoz�, minden egyedet v�letlenszer�en a null�s vagy egyes oszt�lyba sorol
class RandomClassifier:
  def fit(self, x, y):
    return
  def predict(self, x):
    return np.round(np.random.rand(x[:,0].size))

# az egyszer� kezel�s miatt az oszt�lyoz�kat egy t�mbbe tessz�k
# fontos, hogy a fit �s predict f�ggv�nyek azonos m�don h�vhat�ak legyenek
# (azonos interface-t implement�ljanak)
models = []
models.append(RandomClassifier())
models.append(neighbors.KNeighborsClassifier())
models.append(tree.DecisionTreeClassifier())
models.append(lin.LogisticRegression())
models.append(nb.GaussianNB())

# minden modellre elv�gezz�k a tan�t�st (fit),
# majd a tesztadatokhoz j�solunk (predict)
# a j�solt eredm�nyeket ki�rt�kelj�k (accuracy_score)
best_acc = 0
for model in models:
  print(model)
  model.fit(train_features, train_labels)
  pred = model.predict(test_features)
  act_acc = sk_eval.accuracy_score(y_pred = pred, y_true = test_labels)
  print("accuracy: %f" %(act_acc))
  print(sk_eval.classification_report(y_pred = pred, y_true = test_labels))
  print()
  if (act_acc > best_acc):
    best_acc = act_acc
    best_pred = pred
    best_model = model
print()
print("best accuracy: %f" %(best_acc))
print(best_model)

print()
print()
print("--- normalized---")
print()
print()

# a tan�t�- �s a teszadatokat is normaliz�lni kell,
# k�l�nben teljesen semmitmond� eredm�nyeket kapunk
norm_train_features = l2_norm(train_features)
norm_test_features = l2_norm(test_features)

best_acc = 0
for model in models:
  print(model)
  model.fit(norm_train_features, train_labels)
  pred = model.predict(norm_test_features)
  act_acc = sk_eval.accuracy_score(y_pred = pred, y_true = test_labels)
  print("accuracy: %f" %(act_acc))
  print(sk_eval.classification_report(y_pred = pred, y_true = test_labels))
  print()
  if (act_acc > best_acc):
    best_acc = act_acc
    best_pred = pred
    best_model = model
print()
print("best accuracy: %f" %(best_acc))
print(best_model)
