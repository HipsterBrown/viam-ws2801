buf-generate:
	buf generate --template ./src/rgb/proto/buf.gen.yaml ./src/rgb/proto -o ./src/rgb/proto

bundle:
	tar -czf module.tar.gz *.sh .env src requirements.txt

upload:
	viam module upload --version $(version) --platform linux/arm64 module.tar.gz

clean:
	rm module.tar.gz

publish: bundle upload clean
