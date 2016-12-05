
var updateStatus = function (status) {
  linesOfCode = document.getElementsByClassName('list-group-item-status');
  for (var i = 0; i < linesOfCode.length; i++) {
    console.log(linesOfCode[i]);
    linesOfCode[i].className = 'list-group-item-status ' + status.feedback[i];
  }
};

document.getElementById('check-solution-button').onclick = function (e) {
  console.log('Check solution.')
  let data = [];
  var linesOfCode = document.getElementsByClassName('list-group-item-code');
  for (var i = 0; i < linesOfCode.length; i++) {
    numTabs = linesOfCode[i].getElementsByClassName('tabs')[0].dataset.numTabs;
    data[i] = {'num-tabs': numTabs, 'code-line': linesOfCode[i].dataset.codeLine};
  }
  console.log(data);
  $.ajax({
    url: $SCRIPT_ROOT + '/check-solution',
    data: JSON.stringify({answer: data}),
    type: 'POST',
    contentType: 'application/json',
    success: function (response) {
      console.log(response);
      updateStatus(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
};


var leftButtons = document.getElementsByClassName('papr-btn-left');
for (var i = 0; i < leftButtons.length; i++) {
  leftButtons[i].onclick = function (e) {
    console.log(e);
    el = e.target.parentElement.parentElement.getElementsByClassName('tabs')[0];
    if (el.dataset.numTabs > 0) {
      el.dataset.numTabs--;
    }
    el.innerHTML = '&nbsp;'.repeat(el.dataset.numTabs * 4);
  };
};


var rightButtons = document.getElementsByClassName('papr-btn-right');
for (var i = 0; i < rightButtons.length; i++) {
  rightButtons[i].onclick = function (e) {
    console.log(e);
    el = e.target.parentElement.parentElement.getElementsByClassName('tabs')[0];
    el.dataset.numTabs++;
    el.innerHTML = '&nbsp;'.repeat(el.dataset.numTabs * 4);
  };
};


var drake = dragula([document.getElementById('papr')], {
  moves: function (el, container, handle) {
    return handle.classList.contains('handle');
  }
});
