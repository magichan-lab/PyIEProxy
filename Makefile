





clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf `find -name "__pycache__"`
	rm -rf `find -name "*.pyc"`
	rm -rf `find -name ".cache"`
	rm -rf `find -name ".coverage"`
	rm -rf `find -name ".tox"`
