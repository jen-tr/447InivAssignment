from flask import Flask,render_template,request,redirect
from models import db,StudentModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/init')
def populate():
    studentSteve = StudentModel(student_id=211, name="Steve Smith", grade=80)
    studentJian = StudentModel(student_id=122, name="Jian Wong", grade=92)
    studentChris = StudentModel(student_id=213, name="Chris Peterson", grade=91)
    studentSai = StudentModel(student_id=524, name="Sai Patel", grade=94)
    studentAndrew = StudentModel(student_id=425, name="Andrew Whitehead", grade=99)
    studentLynn = StudentModel(student_id=626, name="Lynn Roberts", grade=90)
    studentRob = StudentModel(student_id=287, name="Robert Sanders", grade=75)
    db.session.add(studentSteve)
    db.session.add(studentJian)
    db.session.add(studentChris)
    db.session.add(studentSai)
    db.session.add(studentAndrew)
    db.session.add(studentLynn)
    db.session.add(studentRob)
    db.session.commit()
    return redirect('/')
@app.route('/')
def start():
    return render_template('menu.html')
    
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        grade = request.form['grade']
        student = StudentModel(student_id=student_id, name=name, grade=grade)
        db.session.add(student)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('datalist.html',students = students)
 
 
@app.route('/data/<int:id>')
def RetrieveEmployee(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if student:
        return render_template('data.html', student = student)
    return f"Student with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            name = request.form['name']
            grade = request.form['grade']
            student = StudentModel(student_id=id, name=name, grade=grade)
            db.session.add(student)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Student with id = {id} Does not exist"
 
    return render_template('update.html', student = student)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
app.run(debug = True)
