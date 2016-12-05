BASE_TEMPLATE=template.py
YEAR=2016

# session.cookie must contain the cookie for adventofcode.com in Netscape format

%:
	@if [ -f $*.py ];  \
		then echo "Error: file $*.py exists!"; \
	else \
		cp $(BASE_TEMPLATE) $*.py; \
		sed -i s/CURRENT_DAY/$*/g $*.py; \
		chmod u+x $*.py; \
		touch inputs/sample_$*; \
		wget --load-cookies=session.cookie http://adventofcode.com/2016/day/$*/input -O inputs/input_$*; \
	fi
