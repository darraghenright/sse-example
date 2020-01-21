(function () {
  'use strict';

  const el = document.querySelector('#sse');

  // create an SSE event source object

  const sse = new EventSource('/sse/counter');

  // SSE connection handlers

  sse.onopen = () =>
    el.textContent = 'connection open';

  sse.onerror = () =>
    el.textContent = 'connection error';

  // listen to SSE messages

  sse.addEventListener('counting', ({ data }) =>
    el.textContent = `counting: ${data}`);

  sse.addEventListener('done', () => {
    el.textContent = 'done!';
    sse.close();
  });
})();
