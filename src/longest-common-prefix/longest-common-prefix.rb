# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  lcp = ""

  loop do
    ch = strs[0][lcp.length]

    strs.each do |str|
      return lcp if str.length <= lcp.length || str[lcp.length] != ch
    end

    lcp += ch
  end

  lcp
end
