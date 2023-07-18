from flask import *
from DBConnection import *

app = Flask(__name__)
# static_path="D:\\Riss\\Projects\\Rcm\\static\\"
# static_path="D:\\Midhilesh\\Rcm (2)\\Rcm\\static\\"
static_path="D:\\Riss\\Projects\\Rcm($)\\Rcm3\\Rcm (2)\\Rcm\\static\\"
app.secret_key="123456"


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


@app.route('/')
def hello_world():
    return render_template('launch.html')

@app.route('/username_already/<name>',methods=['GET'])
def username_already(name):
    db = Db()
    qry = "SELECT * FROM `login` WHERE `username`='"+name+"'"
    res = db.selectOne(qry)
    if res is not None:
        print("ppppp")
        return jsonify(status="ok")
    else:
        return jsonify(status="no")


@app.route('/login')
def login():
    return render_template('login index.html')


@app.route('/login_post', methods=['POST'])
def login_post():
    db = Db()
    uname = request.form['username']
    paswrd = request.form['password']
    qry="SELECT * FROM `login` WHERE `username`='"+uname+"' AND `password`='"+paswrd+"'"
    print(qry)
    res=db.selectOne(qry)
    print(res)
    if res is not None:
        session['ln'] = '1'
        if res['type']=='admin':
            session['lid']=res['lid']
            return redirect('/ahome')
        elif res['type']=='manager':
            session['lid'] = res['lid']
            return redirect('/mhome')
        elif res['type']=='volunteer':
            session['lid'] = res['lid']
            # qry1 = "SELECT * FROM`volunteer` WHERE `vol_lid` = '"+str(res['lid'])+"'"
            # res1 = db.selectOne(qry1)
            # session['rcid'] = res1['rcentre_id']
            return redirect('/vhome')
        elif res['type'] == 'guest':
            session['lid'] =  res['lid']
            return redirect('/ghome')
        else:
            return "<script>alert('Invalid login');window.location='/login';</script>"
    else:
        return "<script>alert('No user Found');window.location='/login';</script>"

@app.route('/guest_register')
def guest_register():
    return render_template('register index.html')


@app.route('/guest_register_post', methods=['POST'])
def guest_register_post():
    name = request.form['textfield']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    district = request.form['textfield7']
    photo = request.files['fileField']
    from datetime import  datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    photo.save(static_path + "guest\\" + dt)
    path="/static/guest/" + dt
    db=Db()
    qry="INSERT INTO `login`(`username`,`password`,`type`) VALUES ('"+email+"','"+phone+"','guest')"
    res=db.insert(qry)
    qry1="INSERT INTO `guest`(`guest_lid`,`name`,`email`,`phone`,`place`,`post`,`pin`,`district`,`photo`) VALUES ('"+str(res)+"','"+name+"','"+email+"','"+phone+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+path+"')"
    res1=db.insert(qry1)
    return "<script>alert('Registration complete');window.location='/logout';</script>"


@app.route('/logout')
def logout():
    session.clear()
    session['ln']='0'
    return redirect('/login')

@app.route('/ahome')
def ahome():

    if session['ln']!='0':
        return render_template('admin/Home Index.html')
    else:
        return "Login required"


@app.route('/mhome')
def mhome():
    if session['ln'] != '0':
        return render_template('manager/Home Index.html')
    else:
        return "Login required"



@app.route('/vhome')
def vhome():
    if session['ln'] != '0':
        return render_template('volunteer/Home Index.html')
    else:
        return "Login required"




@app.route('/ghome')
def ghome():
    if session['ln'] != '0':
        return render_template('guest/Home Index.html')
    else:
        return "Login required"



# ============================ Admin  ============================

@app.route('/add_manager')
def add_manager():
    if session['ln']=='0':
        return 'Login required'
    else:
        return render_template('admin/add manager.html')


@app.route('/add_manager_post', methods=['POST'])
def add_manager_post():
    name = request.form['textfield']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    gender = request.form['Gender']
    dob = request.form['textfield4']
    place = request.form['textfield5']
    post = request.form['textfield6']
    district = request.form['textfield7']
    photo = request.files['fileField']
    from datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    photo.save(static_path + "manager\\" + dt)
    path = "/static/manager/" + dt
    db=Db()
    qry = "INSERT INTO `login`(`username`,`password`,`type`) VALUES ('" + email + "','" + phone + "','manager')"
    res = db.insert(qry)
    qry1 = " INSERT INTO `managers`(`lid`,`name`,`dob`,`gender`,`email`,`phone`,`place`,`post`,`district`,`photo`) VALUES('"+str(res)+"','"+name+"','"+dob+"','"+gender+"','"+email+"','"+phone+"','"+place+"','"+post+"','"+district+"','"+path+"') "
    res1 = db.insert(qry1)
    return "<script>alert('Added');window.location='/add_manager';</script>"


@app.route('/admin_view_manager')
def admin_view_manager():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `managers`"
        res = db.select(qry)
        return render_template('admin/View managers.html',data = res)


@app.route('/admin_view_manager_search', methods=['POST'])
def admin_view_manager_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        search = request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `managers` WHERE `name` LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template('admin/View managers.html', data=res)


@app.route('/edit_manager/<lid>')
def edit_manager(lid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `managers` WHERE `lid` ='"+lid+"'"
        res = db.selectOne(qry)
        return render_template('admin/edit manager.html',data = res)


@app.route('/edit_manager_post', methods=['POST'])
def edit_manager_post():
    lid = request.form['lid']
    name = request.form['textfield']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    gender = request.form['Gender']
    dob = request.form['textfield4']
    place = request.form['textfield5']
    post = request.form['textfield6']
    district = request.form['textfield7']
    db = Db()
    from datetime import datetime
    if 'fileField' in request.files:
        photo = request.files['fileField']
        if photo.filename != '':
            dt = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            photo.save(static_path + "manager\\" + dt)
            path = "/static/manager/" + dt
            qry = "UPDATE `managers` SET `name`='"+name+"',`dob`='"+dob+"',`gender`='"+gender+"',`email`='"+email+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`photo`='"+path+"'  WHERE  `lid`='"+lid+"'"
            db.update(qry)
            qry1 = "UPDATE `login` SET `username` ='"+email+"' WHERE `lid` ='"+lid+"'"
            db.update(qry1)
            return "<script>alert('Edited');window.location='/admin_view_manager';</script>"
        else:
            qry = "UPDATE `managers` SET `name`='" + name + "',`dob`='" + dob + "',`gender`='" + gender + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`district`='" + district + "' WHERE  `lid`='" + lid + "'"
            db.update(qry)
            qry1 = "UPDATE `login` SET `username` ='" +email+"' WHERE `lid` ='" + lid + "'"
            db.update(qry1)
            return "<script>alert('Edited');window.location='/admin_view_manager';</script>"
    else:
        qry = "UPDATE `managers` SET `name`='" + name + "',`dob`='" + dob + "',`gender`='" + gender + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`district`='" + district + "' WHERE  `lid`='" + lid + "'"
        db.update(qry)
        qry1 = "UPDATE `login` SET `username` ='" +email+"' WHERE `lid` ='" + lid + "'"
        db.update(qry1)
        return "<script>alert('Edited');window.location='/admin_view_manager';</script>"


@app.route('/delete_manager/<lid>')
def delete_manager(lid):
    db = Db()
    qry = "DELETE FROM `managers` WHERE `lid`='"+lid+"'"
    db.delete(qry)
    qry1 = "DELETE FROM `login` WHERE `lid`='"+lid+"'"
    db.delete(qry1)
    return "<script>alert('deleted');window.location='/admin_view_manager';</script>"


@app.route('/add_notification')
def add_notification():
    if session['ln'] == '0':
        return 'Login required'
    else:
        return render_template('admin/add notification.html')


@app.route('/add_notificaton_post', methods=['POST'])
def add_notificaton_post():
    notification = request.form['textarea']
    db = Db()
    qry="INSERT INTO `notifications`(`notification`,`date`,`time`) VALUES('"+notification+"',CURDATE(),CURTIME())"
    db.insert(qry)
    return "<script>alert('Added');window.location='/add_notification';</script>"


@app.route('/admin_view_notification')
def admin_view_notification():
    if session['ln']=='0':
        return 'Login required'
    else:
        db=Db()
        qry = "SELECT * FROM `notifications`"
        res = db.select(qry)
        return render_template('admin/View Notification.html',data = res)


@app.route('/admin_view_notification_search', methods=['POST'])
def admin_view_notification_search():
    fdate = request.form['textfield']
    tdate = request.form['textfield2']
    db = Db()
    qry = "SELECT * FROM `notifications` WHERE `date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
    res = db.select(qry)
    return render_template('admin/View Notification.html', data=res)


@app.route('/delete_notification/<id>')
def delete_notification(id):
    db = Db()
    qry = "DELETE FROM `notifications` WHERE `notification_id`='"+id+"'"
    db.delete(qry)
    return "<script>alert('deleted');window.location='/admin_view_notification';</script>"


@app.route('/add_rcentre')
def add_rcentre():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `managers`"
        res =db.select(qry)
        return render_template('admin/add relief centers.html',data = res)


@app.route('/add_rcentre_post', methods=['POST'])
def add_rcentre_post():
    name = request.form['textfield']
    phone =request.form['phone']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    district = request.form['textfield5']
    facil = request.form['textarea']
    max_occ = request.form['textfield6']
    voln = request.form['textfield7']
    manager = request.form['manager']
    db = Db()
    qry = " INSERT INTO `relief_center`(`name`,`place`,`post`,`pin`,`district`,`fecilities`,`no_of_volunteers`,`max_occupancy`,`phone`) VALUES('"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+facil+"','"+voln+"','"+max_occ+"','"+phone+"') "
    res=db.insert(qry)
    qry1 = " INSERT INTO `allocate_manager`(`manager_lid`,`centre_id`,`status`) VALUES ('" + manager + "','" + str(res) + "','active')"
    res1 = db.insert(qry1)
    return "<script>alert('Added');window.location='/add_rcentre';</script>"


@app.route('/admin_view_rcentre')
def admin_view_rcentre():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = " SELECT * FROM `relief_center` "
        res = db.select(qry)
        return render_template('admin/View relief centre.html',data = res)


@app.route('/admin_view_rcentre_search', methods=['POST'])
def admin_view_rcentre_search():
    search = request.form['textfield']
    db = Db()
    qry = " SELECT * FROM `relief_center` WHERE `name` LIKE '%"+search+"%'"
    res = db.select(qry)
    return render_template('admin/View relief centre.html', data=res)


@app.route('/edit_rcentre/<id>')
def edit_rcentre(id):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `relief_center` WHERE `id` ='"+id+"'"
        res = db.selectOne(qry)
        qry1 = "SELECT * FROM `managers`"
        res1 = db.select(qry1)
        qry2 = "SELECT * FROM `allocate_manager` WHERE `centre_id` ='"+id+"'"
        res2 = db.selectOne(qry2)
        return render_template('admin/edit relief centers.html',data = res,data1 = res1,data2 = res2)


@app.route('/edit_rcentre_post', methods=['POST'])
def edit_rcentre_post():
    id = request.form['id']
    name = request.form['textfield']
    phone = request.form['phone']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    district = request.form['textfield5']
    facil = request.form['textarea']
    max_occ = request.form['textfield6']
    voln = request.form['textfield7']
    manager = request.form['manager']
    alct_id = request.form['alct_id']
    db = Db()
    qry = "UPDATE `relief_center` SET `name` ='"+name+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`fecilities`='"+facil+"',`no_of_volunteers`='"+voln+"',`pin`='"+pin+"',`max_occupancy`='"+max_occ+"' WHERE `id`='"+id+"'"
    db.update(qry)
    qry1 = "UPDATE `allocate_manager` SET `manager_lid`='"+manager+"' WHERE `alct_id` ='"+alct_id+"'"
    db.update(qry1)
    return "<script>alert('Updated');window.location='/admin_view_rcentre';</script>"


@app.route('/delete_rcentre/<id>')
def delete_rcentre(id):
    db = Db()
    qry = "DELETE FROM `relief_center` WHERE `id`='"+id+"'"
    db.delete(qry)
    return "<script>alert('deleted');window.location='/admin_view_rcentre';</script>"


# @app.route('/assign_manager/<id>')
# def assign_manager(id):
#     db = Db()
#     qry = "SELECT * FROM `managers`"
#     res = db.select(qry)
#     qry1 = "SELECT * FROM `relief_center` WHERE id = '"+id+"'"
#     res1 = db.selectOne(qry1)
#     return render_template('admin/Assign manager.html',data = res, data1 = res1)
#
#
# @app.route('/assign_manager_post', methods=['POST'])
# def assign_manager_post():
#     db = Db()
#     manager = request.form['select']
#     rcentre = request.form['id']
#     qry1 = "SELECT * FROM `allocate_manager` WHERE `manager_lid`='"+manager+"' AND `centre_id` ='"+rcentre+"'"
#     res1 = db.selectOne(qry1)
#     if res1 is None:
#         qry = " INSERT INTO `allocate_manager`(`manager_lid`,`centre_id`,`status`) VALUES ('" + manager + "','" + rcentre + "','active')"
#         res = db.insert(qry)
#         return "<script>alert('Added');window.location='/assign_manager';</script>"
#     else:
#         return "<script>alert('Already added');window.location='/assign_manager';</script>"
#

@app.route('/admin_view_allocation/<rcid>')
def admin_view_allocation(rcid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `allocate_manager` JOIN `managers` ON `managers`.`lid` = `allocate_manager`.`manager_lid` WHERE `allocate_manager`.`centre_id`='"+rcid+"'"
        res = db.selectOne(qry)
        return render_template('admin/View allocation.html',data = res)


@app.route('/delete_allocation/<id>')
def delete_allocation(id):
    db = Db()
    qry = " DELETE FROM `allocate_manager` WHERE `alct_id` = '"+id+"'"
    db.delete(qry)
    return "<script>alert('deleted');window.location='/admin_view_notification';</script>"


@app.route('/admin_view_request')
def admin_view_request():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = " SELECT * FROM `request` JOIN `relief_center` ON `relief_center`.`id`=`request`.`rcentre_id` "
        res = db.select(qry)
        return render_template('admin/View item request.html', data = res)


@app.route('/admin_view_request_search', methods=['POST'])
def admin_view_request_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = " SELECT * FROM `request` JOIN `relief_center` ON `relief_center`.`id`=`request`.`rcentre_id` WHERE `request`.`date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        return render_template('admin/View item request.html', data=res)


@app.route('/admin_view_guest')
def admin_view_guest():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `guest`"
        res = db.select(qry)
        return render_template('admin/view guest.html',data = res)


@app.route('/admin_view_guest_search', methods=['POST'])
def admin_view_guest_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        search = request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `guest` WHERE `name` LIKE  '%"+search+"%'"
        res = db.select(qry)
        return render_template('admin/view guest.html', data=res)


@app.route('/admin_view_volunteers')
def admin_view_volunteers():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `volunteer` JOIN `guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN`relief_center` ON `relief_center`.`id`=`volunteer`.`rcentre_id`"
        res = db.select(qry)
        return render_template('admin/View Volunteers.html' , data = res)


@app.route('/admin_view_volunteers_search', methods=['POST'])
def admin_view_volunteers_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        search = request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `volunteer` JOIN `guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN`relief_center` ON `relief_center`.`id`=`volunteer`.`rcentre_id` WHERE  `guest`.`name` LIKE  '%"+search+"%'"
        res = db.select(qry)
        return render_template('admin/View Volunteers.html', data=res)


@app.route('/admin_view_donations')
def admin_view_donations():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry = " SELECT * FROM `donation` JOIN `guest` ON `guest`.`guest_lid`=`donation`.`guest_lid` "
        res = db.select(qry)
        qry1 = "SELECT * FROM `public_donation`"
        res1 = db.select(qry1)
        return render_template('admin/View Donation.html' , data = res, data1 = res1)


@app.route('/admin_view_donations_search', methods=['POST'])
def admin_view_donations_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = " SELECT * FROM `donation` JOIN `guest` ON `guest`.`guest_lid`=`donation`.`guest_lid` WHERE `donation`.`date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        qry1 = "SELECT * FROM `public_donation` WHERE `date` BETWEEN  '"+fdate+"' AND '"+tdate+"'"
        res1 = db.select(qry1)
        return render_template('admin/View Donation.html', data=res, data1=res1)


@app.route('/admin_add_feedbackqst')
def admin_add_feedbackqst():
    if session['ln'] == '0':
        return 'Login required'
    else:
        return  render_template('admin/add feedback qstn.html')


@app.route('/admin_add_feedbackqst_post', methods=['POST'])
def admin_add_feedbackqst_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        qstn = request.form['qstn']
        db = Db()
        qry = "INSERT INTO `feedbackquestions` (`question`) VALUES ('"+qstn+"')"
        db.insert(qry)
        return "<script>alert('Question added');window.location='/admin_add_feedbackqst#asd';</script>"


@app.route('/admin_view_feedback_qstn')
def admin_view_feedback_qstn():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `feedbackquestions`"
        res = db.select(qry)
        return  render_template('admin/view feedback question.html',data = res)


@app.route('/admin_delete_feedbackqst/<id>')
def admin_delete_feedbackqst(id):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "DELETE FROM `feedbackquestions` WHERE `qid`='"+id+"'"
        db.delete(qry)
        return  "<script>alert('Deleted');window.location='/admin_view_feedback_qstn#asd';</script>"




# ===================================== Manager ============================================

@app.route('/manager_view_profile')
def manager_view_profile():
    if session['ln']=='0':
        return 'Login required'
    else:
        db = Db()
        qry="SELECT * FROM `managers` WHERE `lid` = '"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template('manager/View Profile.html',data = res)


@app.route('/manager_send_request/<rcid>')
def manager_send_request(rcid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        return render_template('manager/request item.html', rcid = rcid)


@app.route('/manager_send_req__post', methods=['POST'])
def manager_send_req__post():

    db = Db()
    item = request.form['textfield']
    types = request.form['textfield2']
    details = request.form['textarea']
    rcid = request.form['rcid']
    qry = "INSERT INTO `request` (`item`,`type`,`details`,`manager_lid`,`rcentre_id`,`date`,`status`) VALUES ('"+item+"','"+types+"','"+details+"','"+str(session['lid'])+"','"+rcid+"',CURDATE(),'pending')"
    db.insert(qry)
    return "<script>alert('Request sent');window.location='/view_assigned_centre';</script>"

@app.route('/manager_update_reqst_status/<id>')
def manager_update_reqst_status(id):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "UPDATE `request` SET `status`='closed' WHERE `req_id` ='"+id+"'"
        res = db.update(qry)
        return "<script>alert('Request updated');window.location='/view_assigned_centre';</script>"


@app.route('/view_assigned_centre')
def view_assigned_centre():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT `relief_center`.*,`relief_center`.`id` AS rcid ,`allocate_manager`.* FROM `relief_center` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`relief_center`.`id` WHERE `allocate_manager`.`manager_lid`= '"+str(session['lid'])+"'"
        res = db.select(qry)
        return render_template('manager/View assigned centre.html',data = res)


@app.route('/view_volunteer_for_centre/<rcid>')
def view_volunteer_for_centre(rcid):
    db = Db()
    qry = " SELECT * FROM `volunteer`  JOIN `guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` WHERE `volunteer`.`rcentre_id`='"+rcid+"'"
    res = db.select(qry)
    return  render_template('manager/View centre Volunteers.html',data = res)


@app.route('/manager_view_notification')
def manager_view_notification():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `notifications`"
        res = db.select(qry)
        return render_template('manager/View Notification.html', data=res)


@app.route('/manager_view_notification_search', methods=['POST'])
def manager_view_notification_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `notifications` WHERE `date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        return render_template('manager/View Notification.html', data=res)


@app.route('/maanager_view_volunteer')
def maanager_view_volunteer():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='"+str(session['lid'])+"' AND `volunteer`.`status`='pending'"
        res = db.select(qry)
        return render_template('manager/View Volunteers.html', data = res)


@app.route('/approve_volunteer/<vid>')
def approve_volunteer(vid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "UPDATE `login` SET `type`='volunteer' WHERE `lid`='"+vid+"'"
        db.update(qry)
        qry1 = "UPDATE `volunteer` SET `status` = 'approved' WHERE `vol_lid` = '"+vid+"'"
        db.update(qry1)
        qry2 = "UPDATE `guest` SET `vstatus` = 'volunteer' WHERE `guest_lid` ='"+vid+"'"
        db.update(qry2)
        return "<script>alert('Approved');window.location='/maanager_view_volunteer';</script>"


@app.route('/reject_volunteer/<vid>')
def reject_volunteer(vid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry1 = "UPDATE `volunteer` SET `status` = 'rejected' WHERE `vol_lid` = '"+vid+"'"
        db.update(qry1)
        return "<script>alert('Rejected');window.location='/maanager_view_volunteer';</script>"


@app.route('/view_approved_volunteer')
def view_approved_volunteer():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='" + str(
            session['lid']) + "' AND `volunteer`.`status`='approved'"
        res = db.select(qry)
        return render_template('manager/View approved Volunteers.html',data =  res)


@app.route('/view_approved_volunteer_search', methods=['POST'])
def view_approved_volunteer_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        search = request.files['textfield']
        qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='" + str(
            session['lid']) + "' AND `volunteer`.`status`='approved' AND `guest`.`name`LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template('manager/View approved Volunteers.html', data=res)


@app.route('/view_rejected_volunteer')
def view_rejected_volunteer():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='" + str(
            session['lid']) + "' AND `volunteer`.`status`='rejected'"
        res = db.select(qry)
        return render_template('manager/View rejected Volunteers.html', data=res)


@app.route('/view_rejected_volunteer_search', methods=['POST'])
def view_rejected_volunteer_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        search = request.files['textfield']
        qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='" + str(
            session['lid']) + "' AND `volunteer`.`status`='rejected' AND `guest`.`name`LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template('manager/View approved Volunteers.html', data=res)


@app.route('/approve_volunteer2/<vid>')
def approve_volunteer2(vid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "UPDATE `login` SET `type`='volunteer' WHERE `lid`='" + vid + "'"
        db.update(qry)
        qry1 = "UPDATE `volunteer` SET `status` = 'approved' WHERE `vol_lid` = '" + vid + "'"
        db.update(qry1)
        return "<script>alert('Approved');window.location='/view_rejected_volunteer';</script>"


@app.route('/reject_volunteer2/<vid>')
def reject_volunteer2(vid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "UPDATE `login` SET `type`='guest' WHERE `lid`='" + vid + "'"
        db.update(qry)
        qry1 = "UPDATE `volunteer` SET `status` = 'rejected' WHERE `vol_lid` = '" + vid + "'"
        db.update(qry1)
        return "<script>alert('Approved');window.location='/view_approved_volunteer';</script>"


@app.route('/manager_view_item_request/<rcid>')
def manager_view_item_request(rcid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `request` JOIN `relief_center` ON `relief_center`.`id`=`request`.`rcentre_id` WHERE `request`.`manager_lid` ='"+str(session['lid'])+"' AND `request`.`rcentre_id` = '"+rcid+"'"
        res = db.select(qry)
        return render_template('manager/View item request.html', data = res)


@app.route('/manager_view_items_send/<rqid>')
def manager_view_items_send(rqid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        print(rqid)
        qry = "SELECT `items_send`.*,`guest`.`name`,`guest`.`phone`,`guest`.`email` FROM `items_send` JOIN `guest` ON `items_send`.`g_lid`=`guest`.`guest_lid` JOIN `request` ON `request`.`req_id` =`items_send`.`request_id` WHERE `items_send`.`request_id`='"+rqid+"'"
        res = db.select(qry)
        return render_template('manager/view_items_send.html',data = res)


@app.route('/volunteer_task_assign/<vid>')
def volunteer_task_assign(vid):
    db = Db()
    # qry = "SELECT `volunteer`.*,`guest`.`name` AS gname,`guest`.`photo`,`guest`.`phone`,`guest`.`email`,`relief_center`.* FROM  `volunteer` JOIN`guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` JOIN `relief_center` ON `relief_center`.`id` = `volunteer`.`rcentre_id` JOIN `allocate_manager` ON `allocate_manager`.`centre_id`=`volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid`='"+str(session['lid'])+"' AND `volunteer`.`status`='approved'"
    # res = db.select(qry)
    return render_template('manager/Assign task for volunteer.html',vol_lid = vid)


@app.route('/volunteer_task_assign_post', methods=['POST'])
def volunteer_task_assign_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        vol_id = request.form['select']
        task =  request.form['textarea']
        db = Db()
        qry = "SELECT * FROM `task` WHERE `vol_lid` = '"+vol_id+"' AND `status`='pending'"
        res = db.selectOne(qry)
        if res is None:
            qry1 = "INSERT INTO `task` (`vol_lid`,`task`,`date`,`status`) VALUES ('"+vol_id+"','"+task+"',CURDATE(),'pending')"
            db.insert(qry1)
            return "<script>alert('Task assigned');window.location='/view_assigned_centre';</script>"
        else:
            return "<script>alert('Already assigned task is pending....!');window.location='/view_assigned_centre';</script>"


@app.route('/manager_view_assigned_task')
def manager_view_assigned_task():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `task` JOIN `volunteer` ON `volunteer`.`vol_lid` =  `task`.`vol_lid` JOIN `guest` ON `guest`.`guest_lid` = `volunteer`.`vol_lid`  JOIN `allocate_manager` ON `allocate_manager`.`centre_id` = `volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid` = '"+str(session['lid'])+"' "
        res = db.select(qry)
        return render_template('manager/view assigned task.html', data = res)


@app.route('/manager_view_assigned_task_search', methods=['POST'])
def manager_view_assigned_task_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `task` JOIN `volunteer` ON `volunteer`.`vol_lid` =  `task`.`vol_lid` JOIN `guest` ON `guest`.`guest_lid` = `volunteer`.`vol_lid`  JOIN `allocate_manager` ON `allocate_manager`.`centre_id` = `volunteer`.`rcentre_id` WHERE `allocate_manager`.`manager_lid` = '" + str(
            session['lid']) + "' AND (`task`.`date` BETWEEN '"+fdate+"' AND '"+tdate+"' ) "
        res = db.select(qry)
        return render_template('manager/view assigned task.html', data=res)


@app.route('/delete_vol_task/<tid>')
def delete_vol_task(tid):
    db = Db()
    qry = " DELETE FROM `task` WHERE `id` = '"+tid+"'"
    db.delete(qry)
    return "<script>alert('Deleted');window.location='/manager_view_assigned_task';</script>"


# =================================== Volunteer =====================================

@app.route('/volunteer_change_password')
def volunteer_change_password():
    # db = Db()
    # qry = ""
    # res = db.selectOne(qry)
    if session['ln']=='0':
        return 'Login required'
    else:
        return render_template('volunteer/change password.html')


@app.route('/volnteer_change_password_post', methods=['POST'])
def volnteer_change_password_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        curpass = request.form['textfield']
        newpass = request.form['textfield2']
        confpass = request.form['textfield3']
        db = Db()
        qry = "SELECT * FROM `login` WHERE `password`='"+curpass+"' AND `lid`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        if res is not None:
            if newpass == confpass:
                qry1 = "UPDATE `login` SET `password` = '"+newpass+"' WHERE `lid` ='"+str(session['lid'])+"'"
                db.update(qry1)
                return "<script>alert('Updated');window.location='/logout';</script>"
            else:
                return "<script>alert('Confirm password error');history.back();</script>"
        else:
            return "<script>alert('Invalid current password');history.back();</script>"


@app.route('/add_refugee')
def add_refugee():
    if session['ln']=='0':
        return 'Login required'
    else:
        return render_template('volunteer/refugee manage.html')

@app.route('/add_refugee_post', methods=['POST'])
def add_refugee_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        name = request.form['textfield']
        gender = request.form['gender']
        age = request.form['textfield2']
        address = request.form['textarea']
        db = Db()
        qry = "INSERT INTO `refugees` (`rname`,`gender`,`address`,`age`,`vol_lid`) VALUES ('"+name+"','"+gender+"','"+address+"','"+age+"','"+str(session['lid'])+"')"
        db.insert(qry)
        return "<script>alert('Added');window.location='/add_refugee';</script>"


@app.route('/volunteer_view_refugees')
def volunteer_view_refugees():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `refugees` WHERE `vol_lid` = '"+str(session['lid'])+"'"
        res = db.select(qry)
        return render_template('volunteer/view refugee.html',data = res)


@app.route('/edit_refugees/<rid>')
def edit_refugees(rid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `refugees` WHERE `rid` ='"+rid+"'"
        res = db.selectOne(qry)
        return render_template('volunteer/edit refugees.html',data = res)


@app.route('/edit_refugees_post', methods=['POST'])
def edit_refugees_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        rid = request.form['rid']
        name = request.form['textfield']
        gender = request.form['gender']
        age = request.form['textfield2']
        address = request.form['textarea']
        db = Db()
        qry = "UPDATE `refugees` SET `rname`='"+name+"',`gender`='"+gender+"',`address`='"+address+"',`age`='"+age+"' WHERE `rid`='"+rid+"'"
        db.update(qry)
        return "<script>alert('Edited');window.location='/volunteer_view_refugees';</script>"



@app.route('/delete_refugee/<rid>')
def delete_refugee(rid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "DELETE FROM `refugees` WHERE `rid`='"+rid+"'"
        db.delete(qry)
        return "<script>alert('Deleted');window.location='/volunteer_view_refugees';</script>"


@app.route('/volunteer_view_assigned_task')
def volunteer_view_assigned_task():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `task` WHERE `vol_lid` ='"+str(session['lid'])+"'"
        res = db.select(qry)
        return render_template('volunteer/view assigned task.html',data = res)


@app.route('/volunteer_view_assigned_task_search', methods=['POST'])
def volunteer_view_assigned_task_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        fdate =request.files['textfield']
        tdate =request.files['textfield2']
        qry = "SELECT * FROM `task` WHERE `vol_lid` ='" + str(session['lid']) + "' WHERE `date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        return render_template('volunteer/view assigned task.html', data=res)


@app.route('/update_task_status/<tid>')
def update_task_status(tid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "UPDATE `task` SET `status` ='Task completed' WHERE `id`='"+tid+"'"
        db.update(qry)
        return "<script>alert('Updated');window.location='/volunteer_view_assigned_task';</script>"


@app.route('/volnteer_view_profile')
def volnteer_view_profile():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT `volunteer`.*,`relief_center`.*,`guest`.`name` AS gname , `guest`.`place` AS gplace, `guest`.`district` AS gdistrict, `guest`.`post` AS gpost FROM `volunteer` JOIN `relief_center` ON `relief_center`.`id` =`volunteer`.`rcentre_id` JOIN `guest` ON `guest`.`guest_lid`=`volunteer`.`vol_lid` WHERE `volunteer`.`vol_lid`='"+str(session['lid'])+"' "
        res = db.selectOne(qry)
        return render_template('volunteer/view profile.html',data = res)


@app.route('/volunteer_edit_profile')
def volunteer_edit_profile():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `guest` WHERE `guest_lid` = '"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template('volunteer/edit profile.html',data = res)


@app.route('/volunteer_edit_profile_post', methods=['POST'])
def volunteer_edit_profile_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        name = request.form['textfield']
        email = request.form['textfield2']
        phone = request.form['textfield3']
        place = request.form['textfield4']
        post = request.form['textfield5']
        pin = request.form['textfield6']
        district = request.form['textfield7']
        db = Db()
        from datetime import datetime
        if 'fileField' in request.files:
            photo = request.files['fileField']
            if photo.filename != '':
                dt = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                photo.save(static_path + "guest\\" + dt)
                path = "/static/guest/" + dt
                qry = "UPDATE `guest` SET `name` ='"+name+"',`email`='"+email+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`district`='"+district+"',`photo`='"+path+"' WHERE `guest_lid`='"+str(session['lid'])+"'"
                db.update(qry)
                qry1 = "UPDATE `login` SET `username` ='"+email+"' WHERE `lid` ='"+str(session['lid'])+"'"
                db.update(qry1)
                return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"
            else:
                qry = "UPDATE `guest` SET `name` ='" + name + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + district + "' WHERE `guest_lid`='" + str(
                    session['lid']) + "'"
                db.update(qry)
                qry1 = "UPDATE `login` SET `username` ='" + email + "' WHERE `lid` ='" + str(session['lid']) + "'"
                db.update(qry1)
                return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"
        else:
            qry = "UPDATE `guest` SET `name` ='" + name + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + district + "' WHERE `guest_lid`='" + str(
                session['lid']) + "'"
            db.update(qry)
            qry1 = "UPDATE `login` SET `username` ='" + email + "' WHERE `lid` ='" + str(session['lid']) + "'"
            db.update(qry1)
            return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"


@app.route('/volunteer_view_notification')
def volunteer_view_notification():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `notifications`"
        res = db.select(qry)
        return render_template('volunteer/View Notification.html',data = res)


@app.route('/volunteer_view_notification_search', methods=['POST'])
def volunteer_view_notification_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `notifications` WHERE `date` BETWEEN '" + fdate + "' AND '" + tdate + "'"
        res = db.select(qry)
        return render_template('volunteer/View Notification.html', data=res)


@app.route('/delete_volunteer_data')
def delete_volunteer_data():

    db = Db()
    qry = "DELETE FROM `volunteer` WHERE `vol_lid` ='"+str(session['lid'])+"'"
    db.delete(qry)
    qry1 = "UPDATE `login` SET `type`='guest' WHERE `lid`='"+str(session['lid'])+"'"
    db.update(qry1)
    return "<script>alert('Volunteer Acoount deleted');window.location='/logout';</script>"





# ================================== Guest ==================================================


@app.route('/guest_view_profile')
def guest_view_profile():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry =  "SELECT * FROM`guest` WHERE `guest_lid` = '"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template('guest/view profile.html',data = res)


@app.route('/guest_edit_profile')
def guest_edit_profile():
    if session['ln'] == '0':
        return 'Login required'
    else:

        db = Db()
        qry = "SELECT * FROM `guest` WHERE `guest_lid` = '"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template('guest/edit profile.html',data = res)


@app.route('/guest_edit_profile_post', methods=['POST'])
def guest_edit_profile_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        name = request.form['textfield']
        email = request.form['textfield2']
        phone = request.form['textfield3']
        place = request.form['textfield4']
        post = request.form['textfield5']
        pin = request.form['textfield6']
        district = request.form['textfield7']
        db = Db()
        from datetime import datetime
        if 'fileField' in request.files:
            photo = request.files['fileField']
            if photo.filename != '':
                dt = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                photo.save(static_path + "guest\\" + dt)
                path = "/static/guest/" + dt
                qry = "UPDATE `guest` SET `name` ='"+name+"',`email`='"+email+"',`phone`='"+phone+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`district`='"+district+"',`photo`='"+path+"' WHERE `guest_lid`='"+str(session['lid'])+"'"
                db.update(qry)
                qry1 = "UPDATE `login` SET `username` ='"+email+"' WHERE `lid` ='"+str(session['lid'])+"'"
                db.update(qry1)
                return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"
            else:
                qry = "UPDATE `guest` SET `name` ='" + name + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + district + "' WHERE `guest_lid`='" + str(
                    session['lid']) + "'"
                db.update(qry)
                qry1 = "UPDATE `login` SET `username` ='" + email + "' WHERE `lid` ='" + str(session['lid']) + "'"
                db.update(qry1)
                return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"
        else:
            qry = "UPDATE `guest` SET `name` ='" + name + "',`email`='" + email + "',`phone`='" + phone + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + district + "' WHERE `guest_lid`='" + str(
                session['lid']) + "'"
            db.update(qry)
            qry1 = "UPDATE `login` SET `username` ='" + email + "' WHERE `lid` ='" + str(session['lid']) + "'"
            db.update(qry1)
            return "<script>alert('Profile updated');window.location='/guest_view_profile';</script>"



@app.route('/guest_change_password')
def guest_change_password():
    # db = Db()
    # qry = ""
    # res = db.selectOne(qry)
    if session['ln']=='0':
        return 'Login required'
    else:
        return render_template('guest/change password.html')


@app.route('/guest_change_password_post', methods=['POST'])
def guest_change_password_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        curpass = request.form['textfield']
        newpass = request.form['textfield2']
        confpass = request.form['textfield3']
        db = Db()
        qry = "SELECT * FROM `login` WHERE `password`='"+curpass+"' AND `lid`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        if res is not None:
            if newpass == confpass:
                qry1 = "UPDATE `login` SET `password` = '"+newpass+"' WHERE `lid` ='"+str(session['lid'])+"'"
                db.update(qry1)
                return "<script>alert('Updated');window.location='/';</script>"
            else:
                return "<script>alert('Confirm password error');history.back();</script>"
        else:
            return "<script>alert('Invalid current password');history.back();</script>"


@app.route('/guest_view_notification')
def guest_view_notification():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `notifications`"
        res = db.select(qry)
        return render_template('guest/View Notification.html',data = res)


@app.route('/guest_view_notification_search', methods=['POST'])
def guest_view_notification_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `notifications` WHERE `date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        return render_template('guest/View Notification.html', data=res)


@app.route('/guest_view_item_request')
def guest_view_item_request():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = " SELECT * FROM `request` JOIN `relief_center` ON `relief_center`.`id`=`request`.`rcentre_id` "
        res = db.select(qry)
        return render_template('guest/View item request.html',data = res)


@app.route('/guest_view_item_request_search', methods=['POST'])
def guest_view_item_request_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        fdate = request.form['textfield']
        tdate = request.form['textfield2']
        db = Db()
        qry = " SELECT * FROM `request` JOIN `relief_center` ON `relief_center`.`id`=`request`.`rcentre_id` WHERE `request`.`date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
        res = db.select(qry)
        return render_template('guest/View item request.html', data=res)


@app.route('/guest_view_rcentre')
def guest_view_rcentre():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = " SELECT * FROM `relief_center` "
        res = db.select(qry)
        return  render_template('guest/View relief centre.html', data = res )


@app.route('/guest_view_rcentre_search', methods=['POST'])
def guest_view_rcentre_search():
    if session['ln'] == '0':
        return 'Login required'
    else:
        search = request.form['textfield']
        db = Db()
        qry = " SELECT * FROM `relief_center` WHERE `name` LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template('guest/View relief centre.html', data=res)


@app.route('/send_volunteer_request')
def send_volunteer_request():
    if session['ln'] == '0':
        return 'Login required'
    else:
        db = Db()
        qry = "SELECT * FROM `relief_center`"
        res = db.select(qry)
        return render_template('guest/volunteer request.html',data = res)


@app.route('/send_volunteer_request_post', methods=['POST'])
def send_volunteer_request_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        rcid = request.form['select']
        db = Db()
        qry1 = "SELECT * FROM `volunteer` WHERE `vol_lid`='"+str(session['lid'])+"'"
        res = db.selectOne(qry1)
        if res is None:
            qry = "INSERT INTO `volunteer` (`vol_lid`,`rcentre_id`,`status`) VALUES ('"+str(session['lid'])+"','"+rcid+"','pending')"
            db.insert(qry)
            return "<script>alert('Request sent for volunteering');window.location='/ghome';</script>"
        else:
            return "<script>alert('Already Volunteer request sent');window.location='/ghome';</script>"


@app.route('/make_donation')
def make_donation():
    if session['ln']=='0':
        return 'Login required'
    else:
        return render_template('guest/donation.html')


@app.route('/make_donation_post', methods=['POST'])
def make_donation_post():
    if session['ln'] == '0':
        return 'Login required'
    else:
        acc_no = request.form['textfield']
        ifsc = request.form['textfield2']
        amount = request.form['textfield3']
        pin = request.form['textfield4']
        print(pin)
        db = Db()
        qry = "SELECT * FROM `bank` WHERE `account_no` = '"+acc_no+"' AND `ifcs_code` = '"+ifsc+"'"
        res = db.selectOne(qry)
        print(res)
        print(res['pin'])
        if res is not None:
            if res['pin'] == int(pin):
                if res['balance']>=int(amount):
                    qry1 = "INSERT INTO `donation` (`amount`,`account_no`,`guest_lid`,`date`) VALUES ('"+amount+"','"+acc_no+"','"+str(session['lid'])+"',CURDATE())"
                    db.insert(qry1)
                    qry2 = "UPDATE `bank` SET `balance`=`balance`-'" + amount + "' WHERE `bank_id` = '" + str(
                        res['bank_id']) + "'"
                    db.update(qry2)
                    return "<script>alert('Donation added.... Thank you.');window.location='/make_donation';</script>"
                else:
                    return "<script>alert('Insufficient Balance to make donation');history.back();</script>"
            else:
                return "<script>alert('Wrong pin entered');window.location='/ghome';</script>"
        else:
            return "<script>alert('Invalid account details');window.location='/ghome';</script>"



def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end = " ")

    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
        return "positive"

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
        return "negative"

    else:
        print("Neutral")
        return "neutral"


@app.route('/useranswertofeedback')
def useranswertofeedback():
    if session['ln'] == '0':
        return 'Login required'
    else:
        qry = "select * from feedbackquestions"
        db = Db()
        res = db.select(qry)
        return render_template("answerfeedback.html", data=res)


@app.route('/usersentfeedback', methods=['POST'])
def usersentfeedback():
    if session['ln'] == '0':
        return 'Login required'
    else:
        id = request.form.getlist("id")
        an = request.form.getlist("a")
        print(id, an)
        db = Db()
        for i in range(0, len(id)):
            s = sentiment_scores(an[i])

            qry = "INSERT INTO `feedbackanswers` (`qid`,`lid`,`answer`,sent) VALUES ('" + id[i] + "','" + str(
                session['lid']) + "','" + an[i] + "','" + s + "')"
            db = Db()
            db.insert(qry)
        return "<script>alert('Feedback sent successfully');window.location='/useranswertofeedback'</script>"


@app.route("/userviewtotalemotiongraph")
def userviewtotalemotiongraph():
    if session['ln'] == '0':
        return 'Login required'
    else:

        l = []
        ans = []

        db = Db()
        qry = "SELECT * FROM `feedbackquestions`"
        res = db.select(qry)
        for i in res:
            l.append(i['question'])

            qry = "SELECT COUNT(*) as 'cnt'  FROM `feedbackanswers`  WHERE `qid`='" + str(
                i['qid']) + "' AND `sent`='negative'"
            res = db.selectOne(qry)
            cntneg = res['cnt']

            qry = "SELECT COUNT(*) as 'cnt'  FROM `feedbackanswers`  WHERE `qid`='" + str(
                i['qid']) + "' AND `sent`='positive'"
            res = db.selectOne(qry)
            cntpos = res['cnt']

            qry = "SELECT COUNT(*) as 'cnt'  FROM `feedbackanswers`  WHERE `qid`='" + str(
                i['qid']) + "' AND `sent`='neutral'"
            res = db.selectOne(qry)
            cntneu = res['cnt']

            ans.append([cntneg, cntneu, cntpos])

        print(len(l))

        return render_template("answergraph.html", l=l, ans=ans, cnt=len(l))
    
    
@app.route('/guest_send_item/<rqid>')
def guest_send_item(rqid):
    if session['ln'] == '0':
        return 'Login required'
    else:
        db=Db()
        qry = "SELECT * FROM `items_send` WHERE `request_id`='"+rqid+"' AND `g_lid`='"+str(session['lid'])+"' AND `date`= CURDATE()"
        res = db.selectOne(qry)
        if res is None:
            qry1 = "INSERT INTO `items_send` (`request_id`,`g_lid`,`date`) VALUES ('"+rqid+"','"+str(session['lid'])+"',CURDATE())"
            db.insert(qry1)
            return '''<script>alert("Your item donation accepted... Volunterrs will contact you soon");window.location="/guest_view_item_request";</script>'''
        else:
            return '''<script>alert("Again, Thank you....");window.location="/guest_view_item_request";</script>'''

# ================================ Public ======================================================


@app.route('/public_donation')
def public_donation():
    return render_template('public donation.html')


@app.route('/public_donation_post', methods=['POST'])
def public_donation_post():
    acc_no = request.form['textfield']
    ifsc = request.form['textfield2']
    amount = request.form['textfield3']
    pin = request.form['textfield4']
    print(pin)
    db = Db()
    qry = "SELECT * FROM `bank` WHERE `account_no` = '" + acc_no + "' AND `ifcs_code` = '" + ifsc + "'"
    res = db.selectOne(qry)
    print(res)
    # print(res['pin'])
    if res is not None:
        if res['pin'] == int(pin):
            if res['balance'] >= int(amount):
                qry1 = "INSERT INTO `public_donation` (`account_no`,`amount`,`date`) VALUES ('"+acc_no+"','"+amount+"',CURDATE())"
                db.insert(qry1)
                qry2 ="UPDATE `bank` SET `balance`=`balance`-'"+amount+"' WHERE `bank_id` = '"+str(res['bank_id'])+"'"
                db.update(qry2)
                return "<script>alert('Donation added.... Thank you.');window.location='/';</script>"
            else:
                return "<script>alert('Insufficient Balance to make donation');history.back();</script>"
        else:
            return "<script>alert('Wrong pin entered');window.location='/';</script>"
    else:
        return "<script>alert('Invalid account details');window.location='/';</script>"

@app.route('/public_view_rcentre')
def public_view_rcentre():
    db = Db()
    qry = " SELECT * FROM `relief_center` "
    res = db.select(qry)
    return render_template('View relief centre.html', data=res)


@app.route('/public_view_notifications')
def public_view_notifications():
    db = Db()
    qry = "SELECT * FROM `notifications`"
    res = db.select(qry)
    return render_template('View Notification.html', data=res)


@app.route('/public_view_notification_search', methods=['POST'])
def public_view_notification_search():
    fdate = request.form['textfield']
    tdate = request.form['textfield2']
    db = Db()
    qry = "SELECT * FROM `notifications` WHERE `date` BETWEEN '"+fdate+"' AND '"+tdate+"'"
    res = db.select(qry)
    return render_template('View Notification.html', data=res)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)

