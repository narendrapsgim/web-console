/**
 * Prevents multiple form submition and add visual information for the user
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('submit', function handleSubmit(event) {
  const SUBMIT_BUTTONS = document.querySelectorAll(`[form=${event.target.id || 'none'}]`)
  for(let button of SUBMIT_BUTTONS) {
    button.disabled = true
    button.classList.add('loading')
  }
})

/**
 * Prevents form submition using only `Enter` key, add submition using
 * combinations of `CMD + Enter`  or `CTRL + Enter`. Allow to use enter in
 * textareas
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('keydown', function handleKeydown(event) {
  if(event.target.localName != 'textarea' && event.target.form && event.keyCode == 13) {
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

/**
 * Updates submit button type if the form has change
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
function handleChange(event) {
  if (event.target.form && event.target.form.classList.contains('persistent')) {
    const SUBMIT_BUTTONS = document.querySelectorAll(`.btn-primary[form=${event.target.form.id || 'none'}]`)

    for(let button of SUBMIT_BUTTONS) {
      button.classList.add('btn-success')
      button.classList.remove('btn-primary')
    }
  }
}

document.addEventListener('change', handleChange)
document.addEventListener('tokenfield:changed', handleChange)

/**
 * Updates form action if clicked Element has a Form and `formaction` attributes
 * (is a submit button). We do so as assigning `formaction` as `action` is done
 * after `submit` event has been triggered and couldn't be used in JS form
 * submission.
 *
 * @param  {Event object} event dispatched submit event
 *
 * @return {undefined}
 */
document.addEventListener('click', function handleClick(event) {
  if (event.target.form && event.target.hasAttribute('formaction')) {
    event.target.form.action = event.target.getAttribute('formaction');
  }
});
