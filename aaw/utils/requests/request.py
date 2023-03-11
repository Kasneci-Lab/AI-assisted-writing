from typing import List, Union, Callable, Dict
import asyncio
from requests_toolkit.openpy import AsyncChatGPT
from requests_toolkit.openpy.config import ChatCompletionConfig
from aaw.globals import APIs,STRINGS
from aaw.utils.utils import get_random_string
from openai.error import InvalidRequestError
import time

class BaseRequestor:
    def __init__(self):
        self.__requestor__ = AsyncChatGPT(
            api_key=APIs['openai'],
            model='gpt-3.5-turbo'
        )

    def __request_no_eval__(self,essay: str, system:str, max_tokens=1000):
        completions = self.__requestor__.reply(ChatCompletionConfig(
            user_name=get_random_string(5),
            user_msg=essay,
            local_system=system,
            temperature=1,
            n=1,
            max_tokens=max_tokens,
            presence_penalty=0,
            frequency_penalty=0
        ))
        return completions


    def request_one(self, essay: str, system:str, max_tokens=1000, error_tmp=None):

        exception = None
        # create a completion
        for i in range(10):
            try:
                completions = self.__request_no_eval__(essay,system,max_tokens).eval()[0]
                return completions,exception

            except InvalidRequestError as ire:
                # If this happens directly stop trying and return
                print("####  Invalid Request!  ####")
                print(ire)
                if error_tmp:
                    error_tmp.error(STRINGS["PROCESS_ERROR"] + str(ire))
                return "", ire
            except Exception as e:
                # For all other exceptions, try multiple times
                print("#####" + str(e) + "#############")
                if error_tmp:
                    error_tmp.error(str(e))
                time.sleep(5)
                if error_tmp:
                    error_tmp.empty()
                exception = e

            return '', exception

    async def __yield_done_generator__(self,tasks):
        """Async generator that yields completed tasks from a list of tasks."""
        completed = set()
        while tasks:
            done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for task in done - completed:
                completed.add(task)
                yield task

    def yield_done(self,tasks, callback:Union[Callable,Dict]):
        async def wrapper():
            async for t in self.__yield_done_generator__(tasks):
                print(f"{t.get_name()} finished.")
                if isinstance(callback,dict):
                    callback_ = callback[t.get_name()]
                    callback_(t)
                else:
                    callback(t)

        loop = asyncio.get_event_loop()
        task= loop.create_task(wrapper())
        loop.run_until_complete(task)

    def __create__empty_string_task__(self):
        async def my_coroutine():
            return ""
        return asyncio.create_task(my_coroutine())

    def request_n(self,essay:str, systems: List[str],max_tokens=1000, error_tmp=None,*, callback:Union[Dict,Callable]):
        tasks = []
        for j in range(len(systems)):
            sys = systems[j]
            task = None
            for i in range(10):
                try:
                    task = self.__request_no_eval__(essay, sys, max_tokens).data
                    break
                except InvalidRequestError as ire:
                    # If this happens directly stop trying and return
                    print("####  Invalid Request!  ####")
                    print(ire)
                    if error_tmp:
                        error_tmp.error(STRINGS["PROCESS_ERROR"] + str(ire))
                    break
                except Exception as e:
                    # For all other exceptions, try multiple times
                    print("#####" + str(e) + "#############")
                    if error_tmp:
                        error_tmp.error(str(e))
                    time.sleep(5)
                    if error_tmp:
                        error_tmp.empty()

            if task is None:
                task = self.__create__empty_string_task__()
            task.set_name(j)
            tasks.append(task)

        self.yield_done(tasks,callback)





