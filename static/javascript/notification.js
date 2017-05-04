function expireNotif(id) {
    $.post('/expireNotification', {
        'id':id
    }, function (res) {
        removeExpiredNotifications(id);
    });
}

function removeExpiredNotifications(id){
    $('#notification-'+id).remove()
}