# Zadanie rekrutacyjne

*Uwaga: dane w projekcie zawrto w katalogu "data/", ze względu na ich wielkość, nie zostały zawarte w repozytorium. W rzeczywsistym projekcie warto by było skorzystać z DVC (jednak nie jest to dobrze mi znana technologia)*
*Uwaga: omyłkowo zakodowano 'Fully paid' jako 1 - uwzględniono to przy modelowaniu*
## Kroki realizacji projektu Data Science
****

**1. Pobranie i wstępny przegląd struktury danych**
Ze względu na obszerność dostarczonego zbioru danych powinien być on wystarczający, w razie jednak jakby w ramach dalszej analizy okazało się że potrzeba rozszerzyć zbiór. Wówczas należałby wrócić do tego kroku i rozszerzyć dane o inne heterogeniczne źródła.
Po wstępnym sprawdzeniu kompletności plików danych, wykluczeniu ew. uszkodzeń i powierzchownej analizie skali liczby brakujących wartości - odłożenie 20% danych (w tym wypadku, gdyż jest ich dużo, w innym razie np 10% lub 5%) jako zbiór testowy. Następnie należy dokonać bardziej szczegółowego przeglądu danych - odrzucić cechy które nie niosą informacji (dużo brakujących wartości, dominacja konkretnej wartości etc.)

W niniejszym zadaniu dokonano w zasadzie ten proces w całości, jedynie w powierzchownej i uproszczonej formie, odrzucając w dość naiwny sposób dane o przekrzywionych rozkładach, zdominowane przez jedną wartość lub te o dużej liczbie brakujących wartości.

**2. Analiza dziedzinowa**
Szczegółowe rozpoznanie dziedziny problemowej, konsultacje z ekspertami, zrozumienie znaczenie poszczególnych zmiennych (dotychczas nieodrzuconych). Rozpoznanie zmiennych które z bardzo dużym prawdpodobieństwem będą miały (lub nie będą miały) znaczenie dla predykcji - odrzucenie tych które są zbędne (z zachowaniem dużej ostrożności *mam pogląd aby bardzo ostrożnie wyrzucać dane, zwłaszcza że wiele modeli dobrze sobie radzi ze zbędnymi atrybutami - oczywiście pamiętając że nie może być ich zbyt dużo*). Odrzucenie zmiennych które są ściśle związane ze zmienną objaśnianą - nie są znane dopóki zmienna objaśniana nie jest znana, można z nich wprost określić zmienną objaśnianą (o ile faktyczne nie powinny być widoczne dla modeli). Wskazanie potencjalnych współzależności. Określenie możliwości uzupełnienia brakujących wartości.

W niniejszym zadaniu ten element został prawie pominięty. Kilka razy spojrzano do opisu zmiennych, aby odrzucić te najmniej przydatne (płytka i naiwna ocena) oraz nie dopuścić do przecieku danych.

**3.Eksploracyjna analiza danych**
Wygenerowanie raportu EDA (Sweetwiz lub Pandas Profiling) aby stanowił on punkt wyjścia do dalszej analizy. Rozpatrzenie potencjalnych przekształceń danych mogących korzystnie wpłynąć na predykcję (np. poprzez doprowadzenie rozkładu do normalnego wykorzystując prostych przekształceń). Rozpoznanie współzależności oraz części cech nieniosących dodatkowej informacji (np. grade i subgrade). Analiza potencjalnego wpływu zmiennych na predykcję i ew. odrzucenie.

W niniejszym zadaniu ten krok wykonano pomijając pogłębioną analizę i ew. przekształcenie zmiennych. Odrzucono cechy podejrzane o to, że nie niosą dodatkowej wiedzy względem pozostałych cech.

**4.Przygotowanie potoku wstępnego przetwarzania danych**
Przygotowanie metod doprowadzający dane do formatu w jakim będą one przetwarzane podczas modelowania. Zdefiniowane wcześniej przekształcenia, kodowanie zmiennych etc. Wyodrębnienie metod jako oddzielne skrypty/klasy ich metody. Konstrukcja potoku przetwarzania metod (ponownie skrypt lub klasa).

Osobiście bym przygotował klasy zawierające odpowiednie metody przetwarzania oraz wywołał je na danych przed podaniem ich do modelu (trening, walidacja, inferencja).

Ten krok wykonano w całości, jednak ze względu na spłycenie poprzednich kroków, był on bardzo prosty i krótki.

**5.Wybór narzędzi/modeli**
W oparciu o doświadczenie, rozpatrywany problem (w tym wypadku klasyfikacja binarna) wybór modeli które mogą przynieść dobre skutki. W tym przypadku wybrałbym regresją liniową, SVM oraz XGBoost i sprawdził ich skuteczność (rozpoczynając od najprostszego i sprawdzając czy bardziej złożone modele poprawiają wynik). Bardziej złożone modele, np. sieci neuronowe zaaplikowane wprost, według autora, nie przyniosłyby dużej poprawy (chociaż w wypadku dostępności czasu i zasobów - warto sprawdzić), ew. można rozpatrzyć czy warto zastosować techniki nlp dla cech zawierających opisy słowne.

**6.Modelowanie/eksperymenty**
Tak jak wyżej wspomniano, należy sprawdzić skuteczność modeli i zbadać czy bardziej złożone model dają szansę na poprawę. Warto również odłożyć zbiór walidacyjny służący strojeniu hiperparametrów, można również wykorzystać walidację krzyżową, jednak pamiętając że nie jest to możliwe dla bardziej złożonych modeli. Warto sprawdzić pojedynczy wpływ hiperparametrów (np. aby mieć podstawy do przygotowania siatki przeszukiwania), a w wypadku dostępności czasu i zasobów przeszukiwanie zachłanne (chyba, że martwimy się o ślad węglowy - wówczas jednak RandomSearch). Należy uwzględnić odpowiednie metryki (w tym wypadku specifity, sensitivity i AUC wydają się rozsądnym wyborem) oraz cel projektu (czy bardziej nam zależy na TP czy TN etc).

**7. Wybór najlepszej metody/Połączenie najlepszych metod**
Ostatecznie należy wskazać najlepszą metodę wraz z ustalonym punktem odcięcia, uwzględniając również złożoność obliczeniową (czas inferencji), ew. kilka metod i połączyć w model zespołowy.

**8.Wdrożenie modelu**
Parametry modelu należy zapisać (oraz stworzyć kopie zapasowe). Następnie umożliwić korzystanie z jego funkcjonalności. Najlepiej wystawić model jako restowe api i ew. dorobić prosty frontendowy interfejs. Ew. dostarczyć metodę jako paczkę danego języka programowania (jeśli predykcja ma posłużyć jak funkcjonalność istniejącego systemu, tak aby można było łatwo wprowadzić jego metody do istniejącego kodu).
