.PHONY: all run clean

SS = SolarSystem
OPT = output

all:
	make clean
	make run
	make visualize

run:
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
	rm -f ./output/*