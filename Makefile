TARGET=results/sample.png
VIDEO_TARGETS=results/seed.mp4

BIN=scripts
DATA=datas
RST=results
NOTE=$(RST)/test_result
TESTER=./test/verify.py

SOGITREE=./SogiTree
TREE2PNG=./tree2png
TREE2HTML=./tree2html

.PRECIOUS : %.ppm
.PHONY : all note clean view web

all : $(TARGET)

video : $(VIDEO_TARGETS)

clean :
	rm -rf $(RST)/*

$(RST)/%.png : $(DATA)/%.tree
	$(TREE2PNG) $< $@

$(RST)/%.mp4 : datas/%.tree
	DIR=$$(echo $@ | sed -e 's/.mp4//') ;\
	mkdir -p $$DIR ;\
	for I in $$(seq -w 1 30) ; \
	do \
		if [ $$I -eq 1 ] ;\
		then \
			TREE_IN=$$DIR/$$I.tree ;\
			cp $< $$TREE_IN ;\
			$(TREE2PNG) $$TREE_IN $$TREE_IN.png ;\
		else \
			TREE_OUT=$$DIR/$$I.tree ;\
			$(SOGITREE) < $$TREE_IN > $$TREE_OUT ;\
			$(TREE2PNG) $$TREE_OUT $$TREE_OUT.png ;\
			TREE_IN=$$TREE_OUT ;\
		fi \
	done ;\
	ffmpeg -r 10 -i $$DIR/%0$${#I}d.tree.png -r 10 $@ ;\
	convert -delay 10 -loop 0 $$DIR/*.png $$DIR.gif

$(RST)/%.html : $(DATA)/%.tree
	$(TREE2HTML) $< $@ tree.css

README.pdf : README.md
	pandoc -t beamer $< --highlight-style=zenburn -o $@

note:
	rm -f $(NOTE)
	$(SOGITREE) < $(DATA)/desert.tree > $(RST)/desert_test.tree
	$(SOGITREE) < $(DATA)/seed.tree > $(RST)/seed_test.tree
	$(SOGITREE) < $(DATA)/sample.tree > $(RST)/sample_test.tree

	$(TESTER) $(DATA)/seed.tree $(RST)/seed_test.tree >> $(NOTE)
	$(TESTER) $(DATA)/desert.tree $(RST)/desert_test.tree >> $(NOTE)
	$(TESTER) $(DATA)/sample.tree $(RST)/sample_test.tree >> $(NOTE)

	@echo "ERREURS = " $$(cat $(NOTE) | sort | uniq | grep "FAILED" | wc -l)
	@echo "TESTS OK= " $$(cat $(NOTE) | sort | uniq | grep "SUCCESS" | wc -l)

generate:
	./scripts/terraform.py > new_world.tree
	cat new_world.tree | ./SogiTree > new_world.processed
	./tree2png new_world.processed new_world.png
	eog new_world.png
