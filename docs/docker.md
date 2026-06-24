
To create the docker image, clone the project and move to the root directory

git clone ...
cd ..

```bash
git clone 

```
Move to the root directory of the project

```bash
cd

```
Create docker image
```bash

docker build . -t py-html-to-pdf 

```

Run it on your local with this command
```bash
docker run --rm -p 5000:5000 --name pdf py-html-to-pdf

```

Open a new terminal and Test the api
```bash

curl http://localhost:5000/api-pdf/v1/health

```

```bash

curl -X POST http://localhost:5000/api-pdf/v1/html-to-pdf/convert   -H "Content-Type: application/json"   -d '{"html": "<h1>TEST MY APP </h1><p>Content test</p>"}'   --output output.pdf

```

### docker build . -t py-html-to-pdf 
### docker push briandwamba/nemesis:ges-loca-pdf
### docker run --rm -p 5000:5000 --name pdf briandwamba/nemesis:ges-loca-pdf

