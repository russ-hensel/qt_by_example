These are the developer notes and scratch pad.

Maybe there is something useful here or not

Table of Contents

---- How these examples are constructed.
---- Work in the pipeline
---- Scratch

=================================================



---- How these examples are constructed.
        Note:
            I am in the middle of a lot of refactoring, these notes are sometime
            a bit insperational, not all of the work is complete yet.

    The "runable" apps here are


       qt_widgets.py


        Individual tabs are now all in ( or being moved into ) their own modules
            like:
                tab_combo_box.py
                .... they all begin with tab_

        utilities that help eveything run are in:

            utils_for_tabs as uft.py
            parameters.y


    the main window for an app, like QtWidgetExamples, QMainWindow and
    its gui is largely base on a QTabWidget.  This widget then
    is used as a container for all the tabs in all the modules.

    You can use the application itself as a tutorial on how a window
    with tabpages might be implemented.



    The wat-inspector applications.

        All the qt examples use the wat-inspector so you can use any one
        of them as a tutorial on how to use the wat-inspector.

        Additionally there are 2 simpler apps that might be a better
        place to start if it is only the wat inspector that interests
        you.

            qt_wat.py
            qt_wat_app.py

    Couple of other modules I am woking into wat-inspector.py:

        info_about.py
        info_about_qt.py

            they do some custom inspection of some classes -- may becoume useful
            in the future.  They are linked to a button that might be called <cust inspect>


    wat_inspector.py is the module with the inspector code it is use by



/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/info_about.py




===============================================================


---- Work in the pipeline

    see general help for each app


        break examples into their own tabs

add this to icons
p.yusukekamiyamane - Free stock icons + pixel fonts
https://p.yusukekamiyamane.com/


wat ideas

        compose into eval from inspection results  -- context menu?
        have ddl as memory to entries


        smooth off edges of gui on what alread have

        pass in a script
        break on exit



    io_qt

        continue migration expansion

qt_exammple ideas

        to many for here, perhaps in helps

When you call self.accept() on a QDialog, it closes the dialog, but it also means that the dialog instance cannot be reused directly to open it again. To open the dialog multiple times, you generally have two options:

    Create a New Instance Each Time: This is the simplest approach. Every time you want to show the dialog, you create a new instance of it.

def open_dialog(self):
    dialog = MyDialog(self)
    if dialog.exec():
        # Process the result if needed
        print("Dialog accepted.")

Use QDialog::hide() Instead of QDialog::accept(): If you want to reuse the same instance of the dialog, call self.hide() instead of self.accept() to close it. Then, you can reopen it by calling self.show() or self.exec() again.

    # Inside the dialog class
    def close_dialog(self):
        self.hide()  # Instead of self.accept()

    # Reopen the dialog
    dialog.show()  # Or dialog.exec() to reopen modally

In many cases, option 1 is simpler and more reliable because it ensures a fresh instance every time. However, if the dialog has a lot of complex setup that you want to preserve, option 2 can work well with minor adjustments.




how to install wat
    conda forge on fattony ok

------------------ xxx ----------------------



SELECT
    people.id,
    people.name,
    people.age,
    people.family_relation,
    people_phones.phone_number
FROM people
LEFT JOIN people_phones ON people.id = people_phones.person_id


I have a QSqlRelationalTableModel that implement the select above.

Some of the code is

        model           = QSqlRelationalTableModel(self)
        self.model      = model
        # self.model          = qt_with_logging.QSqlRelationalTableModelWithLogging(
        #     self )
        model.setTable( "people" )

        debug_var   = self.model.fieldIndex( "id" )   # field name to number

        model.setRelation(
            self.model.fieldIndex( "id" ),  # column name in first table, here people

            QSqlRelation("people_phones", "person_id",      "phone_number")

How can I insert a new record and then update the database.  Can you show the code?


----------------------- chat  ------------------
from PyQt5.QtSql import QSqlRecord, QSqlField

# Assuming `model` is your QSqlRelationalTableModel instance for the `people` table

# Create a new empty record for the 'people' table
new_record = model.record()

# Set values for each field in the new record
new_record.setValue("id", 123)                # Replace 123 with the actual ID value
new_record.setValue("name", "John Doe")       # Set name
new_record.setValue("age", 30)                # Set age
new_record.setValue("family_relation", "Brother")  # Set family relation

# Insert the new record at the end of the table
if model.insertRecord(-1, new_record):
    # Try to submit all changes to the database
    if model.submitAll():
        print("Record inserted and changes committed to the database.")
    else:
        print("Error committing changes:", model.lastError().text())
else:
    print("Error inserting record:", model.lastError().text())


------------------------gpt ---------------------------

-------1 did not use the widget
i asked to try again
deleted

--------2

import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtCore import Qt

def create_connection():
    # Connect to an SQLite database or replace this with your database details
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("your_database.db")

    if not db.open():
        print("Unable to connect to the database")
        return False

    return True

def setup_model():
    # Create the QSqlRelationalTableModel for the `people` table
    model = QSqlRelationalTableModel()
    model.setTable("people")

    # Define a relationship between people and people_phones using QSqlRelation
    # Assuming `person_id` in `people_phones` is a foreign key referencing `people.id`
    model.setRelation(model.fieldIndex("id"), QSqlRelation("people_phones", "person_id", "phone_number"))

    # Select the data to apply the relation
    model.select()

    # Set headers for display in the view
    model.setHeaderData(model.fieldIndex("id"), Qt.Horizontal, "ID")
    model.setHeaderData(model.fieldIndex("name"), Qt.Horizontal, "Name")
    model.setHeaderData(model.fieldIndex("age"), Qt.Horizontal, "Age")
    model.setHeaderData(model.fieldIndex("family_relation"), Qt.Horizontal, "Family Relation")
    model.setHeaderData(model.fieldIndex("phone_number"), Qt.Horizontal, "Phone Number")

    return model

def main():
    app = QApplication(sys.argv)

    # Ensure connection to the database
    if not create_connection():
        sys.exit(1)

    # Set up the model and view
    model = setup_model()
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle("People and Phones")
    view.resize(800, 400)
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



-----------------------------------------------





WHERE people.id = 2;


        query.exec_("""
            CREATE TABLE people (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                age             INTEGER,
                family_relation TEXT
            )
        """)

        # Create the 'people_phones' table with a foreign key to the 'people' table
        query.exec_("""
            CREATE TABLE people_phones (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id       INTEGER,
                phone_number    TEXT,
                FOREIGN KEY(person_id) REFERENCES people(id) ON DELETE CASCADE
            )
        """)



   #------------
   def populate_people_phones_table( self, ):
       """
       Populate the people_phones table.
       """
       what    = "populate_people_phones_table"
       print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

       query = QSqlQuery( self.db )

       table_data = [
           (1, "555-1234", "A"), (1, "555-5678", "B"), (1, "555-8765", "C"),
           (2, "555-4321", "A"), (1, "555-8765", "B"), (2, "555-3456", "C"),
           (3, "555-9876", "A"), (3, "555-1111", "B"), (3, "555-2222", "C"),
           (4, "555-3333", "A"), (4, "555-4444", "B"), (4, "555-5555", "C"),
           (5, "555-6666", "A"), (5, "555-7777", "B"), (5, "555-8888", "C"),
           (5, "555-9999", "A"), (5, "555-0000", "B"), (5, "555-1235", "C"),
           (2, "555-2345", "A"), (1, "555-3456", "B")
       ]

       sql   = """INSERT INTO people_phones (
                     person_id,
                     phone_number,
                     zone )
                    VALUES ( ?, ?, ? )
       """

       # this  is the positional style with bind values
       for person_id, phone_number, zone in table_data:
           query.prepare( sql )
           # bind value for each ?
           query.addBindValue( person_id )
           query.addBindValue( phone_number)
           query.addBindValue( zone )
           query.exec_()
