function validation() {
  name=document.getElementById('name_field').value
  email=document.getElementById('email_field').value
  contactno=document.getElementById('contactno_field').value
  message=document.getElementById('message_field').value

  email_reg=/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/

  if(name.trim()=='')  {
    document.getElementById('name_error').style.cssText="visibility:visible;color:red;"
    return false
  }
  else if(email_reg.test(email)==false) {
    document.getElementById('name_error').style.cssText="visibility:hidden;"
    document.getElementById('email_error').style.cssText="visibility:visible;color:red;"
    return false
  }
  else if(!contactno.match(/^\d{10}$/)) {
    document.getElementById('email_error').style.cssText="visibility:hidden;"
    document.getElementById('contactno_error').style.cssText="visibility:visible;color:red;"
    return false
  }
  else if(message.trim()=='') {
    document.getElementById('contactno_error').style.cssText="visibility:hidden;"
    document.getElementById('message_error').style.cssText="visibility:visible;color:red;"
    return false
  }
  else {
      alert("Your Response has been saved!")
      return true
  }
}

function loginvalidation() {
  username=document.getElementById('username_id').value
  password=document.getElementById('password_id').value

  if(username==''||password=='')  {
    document.getElementById('message').style.cssText="visibility:visible;color:red;"
    return false
  }
  else {
    return true
  }
}
