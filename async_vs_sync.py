import httpx
import asyncio
import logging # logging lib is for logging the events in the code, which can be helpful for debugging and understanding the flow of the program.
import scalene # scalen lib is for profiling. #if you want to see how much time every function takes,
#run this script in terminal 'scalene run --outfile profile async.py', and open with 'scalene view profile.json'

logging.basicConfig(
    filename="api.log",
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)


urls = {
    "FirstAPI":  f"https://ExampleAPI.com",
    "SecondAPI": f"https://ExampleAPI.com/0",
    "ThirdAPI":  f"https://ExampleAPI.com/1",
    "ForthAPI":  f"https://ExampleAPI.com/2"
    }


headers = {'User-Agent': 'Mozilla/5.0'}

def synchronous():
    # synchronous code to fetch data from APIs
    logging.info("info :: Start synchronous FUNC")
    for api_name,api_url in urls.items():
        logging.info(f"info :: Fetching {api_name} Starts")
        response = httpx.get(api_url,headers=headers)
        logging.info(f"info :: Fetching {api_name} Ends and Status is {response}")

async def get_single_api(client: httpx.AsyncClient, name, url):
    logging.info("info :: Start get_single_api FUNC")
    logging.info("info :: Start Semaphore context manager")
    response = await client.get(url,headers=headers)
    logging.info(f"info :: Fetching {name} Ends and Status is {response}")

async def asynchronous(): 
    logging.info("info :: Start asyncrounes FUNC")
    # Gather Tasks
    tasks = []
    async with httpx.AsyncClient() as client:
        logging.info("info :: Start client context manager")
        
        for api_name,api_url in urls.items():
            logging.info("info :: Loop to Creating Task")

            task = asyncio.create_task(get_single_api(client, api_name, api_url))
            tasks.append(task)
            logging.info( f"info :: Task {api_name} Created!")

        logging.info("info :: Gathering Tasks")
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    synchronous()
    asyncio.run(asynchronous())