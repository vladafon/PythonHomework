import uvicorn

uvicorn.run("fake_data_serv.application:app",
            debug=True,
            reload=True
            )