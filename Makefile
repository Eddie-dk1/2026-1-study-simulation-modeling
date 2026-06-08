
.PHONY: help generate render verify clean

help:
	@printf "Targets:\n"
	@printf "  make generate  - recreate repository structure and generated assets\n"
	@printf "  make render    - build html/docx/pptx outputs with pandoc\n"
	@printf "  make verify    - run structural and content checks\n"
	@printf "  make clean     - remove generated cache\n"

generate:
	python3 tools/generate_course_repo.py

render:
	python3 tools/render_outputs.py

verify:
	python3 tools/verify_repo.py

clean:
	rm -rf .cache tools/generated
