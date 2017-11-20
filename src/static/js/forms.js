/**
 * Prevents multiple form submition and add visual information for the user
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('submit', function handleSubmit(event) {

  if (event.target.method in ['post', 'get']) {
    const SUBMIT_BUTTON = document.querySelector(`[form=${event.target.id}]`)
    SUBMIT_BUTTON.disabled = true
    SUBMIT_BUTTON.classList.add('loading')
  }
})

/**
 * Prevents form submition using only `Enter` key, add submition using
 * combinations of `CMD + Enter`  or `CTRL + Enter`
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('keydown', function handleKeydown(event) {
  if(event.target.form && event.keyCode == 13) {
    if (event.metaKey || event.ctrlKey) {
      event.target.form.submit()
    } else {
      event.preventDefault()
    }
  }
})

/**
 * Prevents leaving the page if a `.persistent` form has changed, allow to
 * submit the form.
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('change', function handleChange(event) {

  function handleBeforeUnload(event) {
    var confirmationMessage = 'Changes you made may not be saved.'

    event.returnValue = confirmationMessage  // Gecko, Trident, Chrome 34+
    return confirmationMessage               // Gecko, WebKit, Chrome <34
  }

  if (event.target.form && event.target.form.classList.contains('persistent')) {
    window.addEventListener('beforeunload', handleBeforeUnload)
    document.addEventListener('submit', function handleSubmit(event) {
      window.removeEventListener('beforeunload', handleBeforeUnload)
    })
  }
})