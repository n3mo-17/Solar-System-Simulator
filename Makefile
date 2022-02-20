.PHONY: all clean

SS = SolarSystem
OPT = output

all:
	make clean
	make run
	make visualize

$(OPT):
	mkdir output

run: $(OPT)
	python ./run_sim.py

$(OPT)/*.txt:
	make run

$(OPT)/graphs:
	mkdir output/graphs

visualize: $(OPT)/*.txt $(OPT)/graphs
	python ./visualize.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf ./SolarSystem/__pycache__
	rm -f ./output/*.txt
	rm -f ./output/graphs/*