export default function getStudentIdsSum(list) {
  list.reduce((total, student) => total + student.id, 0);
}
