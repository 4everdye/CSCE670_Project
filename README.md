CSCE670_Project
===============

People Search

1. Required packages: requests, beatifulsoup4
2. Prequisite: Stanford Named Entity Recognizer (NER): http://nlp.stanford.edu/software/CRF-NER.shtml
3. Run the following script in console:   

java -mx1000m -cp stanford-nr.jar edu.stanford.nlp.ie.NERServer -loadClassifier    classifiers/english.all.3class.distsim.crf.ser.gz -port 1234 -outputFormat inlineXML
4. Run the Main.py without parameters and then input query
