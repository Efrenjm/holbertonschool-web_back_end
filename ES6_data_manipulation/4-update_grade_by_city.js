export default function updateStudentGradeByCity(students, city, newGrades) {
  students
    .filter((student) => student.location === city)
    .map((item) => {
      const newRecord = { ...item };

      const newStudent = newGrades.find((student) => student.studentId === item.id);
      newRecord.grade = newStudent ? newStudent.grade : 'N/A';

      return newRecord;
    });
}
