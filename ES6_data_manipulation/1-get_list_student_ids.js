export default function getListStudentId(getList) {
  let lisdata = [];
  if (!(getList instanceof Array)) {
    return lisdata;
  }
  lisdata = getList.map((results) => results.id);
  return lisdata;
}
