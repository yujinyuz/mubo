.PHONY: app

app:
	@echo "Creating app under src/mubo/apps/$(name)"
	@mkdir -p src/mubo/apps/$(name)
	@python manage.py startapp $(name) src/mubo/apps/$(name)

