from time import sleep

def sse_message(id: int, event: str, data: any='') -> str:
    '''
    Create a SSE format message
    '''
    return (
        f'id: {id}\n'
        f'event: {event}\n'
        f'data: {data}\n\n'
    )

def sse_counter(max_count: int=3) -> str:
    '''
    Counter as a stream of SSE messages
    '''
    id, counter = 1, 0

    while counter <= max_count:
        yield sse_message(id, 'counting', counter)
        counter += 1
        sleep(1)

    yield sse_message(id, 'done')
