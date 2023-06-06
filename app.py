from flask import Flask ,jsonify,redirect
app = Flask(__name__)
# testing with a list of dictionnaries as a db
db =[{'id':0,
            'firstname':'firstnameTest',
            'lastname':'lastnameTest'
    },
    ]
@app.route('/api/v1/')
def home():
    return "WELCOME TO MY APP \n EVERYTHING\'S FINE" 

# route pour afficher la db 
@app.route('/api/v1/employees/', methods=['GET'])
def get_employee():
    return jsonify(db)

# route for afficher un seul employée
@app.route('/api/v1/employees/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person =  [a for a in db if a['id']==person_id]
    return jsonify(person[0]) if  len (person)!=0 else 'No employees Have this id'

# route pour creer un employee
@app.route('/api/v1/employees/<int:emp_id>&<emp_first_name>&<emp_last_name>', methods=['POST'])
def create_employee(emp_id,emp_first_name,emp_last_name):
    new_employee = {
        "id": emp_id,
        "first_name": emp_first_name,
        "last_name": emp_last_name
    }
    db.append(new_employee)
    return (f"employee created successfully \n {new_employee}") 

# route pour update un employee
@app.route('/api/v1/employees/<int:person_id>&<emp_first_name>&<emp_last_name>', methods=['PUT'])
def update_employee(person_id,emp_first_name,emp_last_name):
    employee = [a for a in db if a['id'] == person_id]
    employee[0]['first_name']=emp_first_name
    employee[0]['last_name']=emp_last_name
    return jsonify(employee[0])

# route pour supprimer un employee
@app.route('/api/v1/employees/<int:person_id>', methods=['DELETE'])
def delete_employee(person_id):
    employee = [a for a in db if a['id'] == person_id]
    db.remove(employee[0])
    return 'Employee deleted'

##########################
if __name__ == "__main__":
    app.run(debug=True)